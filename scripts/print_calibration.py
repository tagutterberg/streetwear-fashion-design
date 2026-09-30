"""Create and check an A4 vector print-scale test, not a sewing pattern."""
import argparse
from pathlib import Path
from xml.sax.saxutils import escape
import reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, NameObject

MM = 72 / 25.4


def generate(output):
    output.mkdir(parents=True, exist_ok=True)
    font = Path(reportlab.__file__).parent / 'fonts' / 'Vera.ttf'
    pdfmetrics.registerFont(TTFont('Calibration', str(font)))
    # One list of millimetre coordinates feeds both vector formats.
    shapes = [
        ('text', 15, 20, 12, 'Design by Gutteberg / Utskriftskontroll'),
        ('text', 15, 30, 9, 'A4 210 x 297 mm. Skriv ut i faktisk størrelse / 100 %.'),
        ('text', 15, 38, 8, 'Slå av Tilpass, Krymp og forstørring for kantløs utskrift.'),
        ('rect', 55, 70, 100, 100),
        ('text', 73, 120, 12, '100 x 100 mm'),
        ('text', 57, 133, 8, 'Mål fra linjens midte til midte.'),
        ('line', 15, 200, 195, 200),
        ('line', 25, 45, 25, 225),
        ('text', 60, 212, 9, 'Vannrett kontroll: 180 mm'),
        ('text', 36, 224, 9, 'Loddrett kontroll: 180 mm'),
        ('text', 15, 244, 9, 'Kontrollkvadrat: vannrett ____ mm / loddrett ____ mm'),
        ('text', 15, 254, 8, 'Godkjent når begge sider er 99,5–100,5 mm. Kontroller også 180 mm.'),
        ('text', 15, 264, 8, 'Skriver / papir: _______________________ Dato: ______________'),
        ('text', 15, 281, 8, 'Dette kontrollerer utskriftsskalaen. Plaggets passform må prøves separat.'),
    ]
    for x in range(15, 196, 10): shapes.append(('line', x, 197, x, 203))
    for y in range(45, 226, 10): shapes.append(('line', 22, y, 28, y))
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">', '<rect width="210" height="297" fill="white"/>', '<g fill="none" stroke="#26333d" stroke-width="0.25">']
    pdf_path = output / 'utskriftskontroll-a4.pdf'
    c = canvas.Canvas(str(pdf_path), pagesize=(210 * MM, 297 * MM))
    c.setTitle('Design by Gutteberg - utskriftskontroll 1:1')
    c.setLineWidth(.25 * MM)
    for shape in shapes:
        kind, *a = shape
        if kind == 'rect':
            x, y, w, h = a
            svg.append(f'<rect id="calibration-square" x="{x}" y="{y}" width="{w}" height="{h}"/>')
            c.rect(x * MM, (297-y-h) * MM, w * MM, h * MM)
        elif kind == 'line':
            x1, y1, x2, y2 = a
            svg.append(f'<path d="M{x1} {y1}L{x2} {y2}"/>')
            c.line(x1 * MM, (297-y1) * MM, x2 * MM, (297-y2) * MM)
        else:
            x, y, pt, text = a
            svg.append(f'<text x="{x}" y="{y}" fill="#26333d" stroke="none" font-family="Bitstream Vera Sans,Arial,sans-serif" font-size="{pt/MM:.8f}">{escape(text)}</text>')
            c.setFont('Calibration', pt)
            c.drawString(x * MM, (297-y) * MM, text)
    svg.append('</g></svg>')
    (output / 'utskriftskontroll-a4.svg').write_text('\n'.join(svg), encoding='utf-8')
    c.save()
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    writer.append(reader)
    writer._root_object[NameObject('/ViewerPreferences')] = DictionaryObject({NameObject('/PrintScaling'): NameObject('/None')})
    writer.write(pdf_path)
    check = PdfReader(pdf_path)
    page = check.pages[0]
    assert abs(float(page.mediabox.width) - 210 * MM) < .001
    assert abs(float(page.mediabox.height) - 297 * MM) < .001
    rectangles = [operands for operands, op in page.get_contents().operations if op == b're']
    assert any(abs(float(r[2])-100*MM) < .001 and abs(float(r[3])-100*MM) < .001 for r in rectangles)
    assert not page.images
    assert check.trailer['/Root']['/ViewerPreferences']['/PrintScaling'] == '/None'
    print(f'PASS: A4, 100 mm vector square, no raster images, print scaling disabled. {pdf_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    generate(parser.parse_args().output)
