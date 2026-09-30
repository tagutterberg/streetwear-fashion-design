# Print-ready sewing patterns

## Drafting and status

A full-size sewing pattern requires confirmed measurements or a documented size/base pattern, a stated drafting method, and checked construction geometry. A calibration square proves scale, not fit. Keep schematic overviews and illustration PDFs separate from the pattern print package. Missing measurements mean the corresponding draft remains provisional.

Check stitch-line seam lengths, deliberate easing, darts/folds, notch correspondence, closure placement, and allowance geometry before marking construction checked. Recommend a toile for fitted or expensive garments. Do not describe a digitally checked draft as physically printed or fitted without reported measurements.

## One physical coordinate system

Draft and store geometry in millimetres. Root SVG physical size must agree with the viewBox: `width="800mm" height="1400mm" viewBox="0 0 800 1400"` establishes one coordinate unit per millimetre. Use physical page dimensions and the same geometry for every output. [W3C SVG coordinate specification](https://www.w3.org/TR/SVG2/coords.html)

Use stable groups/IDs for construction, cutting, annotations, and each pattern piece. Keep source text editable. Avoid display-responsive units or accidental scale transforms in production geometry. Rotation/translation for page layout are allowed; resizing to fit is not.

Default printed text sizes, expressed in millimetre user units:

| Purpose | Points | SVG user units |
| --- | ---: | ---: |
| Piece label | 9 pt | 3.175 |
| Notes and seam markers | 8 pt | 2.8222 |
| Piece title | 12 pt | 4.2333 |

Keep text clear of cut/stitch lines, notches, and drill marks; move dense instructions to their own document. Embed fonts in PDF. Suggested line widths: 0.35 mm cutting, 0.20 mm construction, 0.25 mm markings; distinguish lines through dash patterns/labels as well as color.

## Export package

Generate editable SVG, vector A4 tiles, vector A0 pages, and a separate illustrated instruction PDF from the same checked geometry. Existing ReportLab can draw vector PDF from the same measured paths/points used for SVG; use an established vector exporter when a supplied SVG needs conversion. Do not rasterize production paths or build a general SVG converter unnecessarily.

PDF conversion uses exactly `72 / 25.4` points per millimetre. Verify page MediaBox/CropBox and the coordinate transforms; do not auto-fit, crop away geometry, or set PDF UserUnit to an unverified value. Set PDF print preference `/PrintScaling /None` when supported, but still require a calibration print because viewers/drivers can override it.

### A4 home printing

- Page size: 210 × 297 mm; 10 mm safe margins; usable region 190 × 277 mm.
- Adjacent tiles overlap by 10 mm; grid steps are 180 × 267 mm. Translate/clip the unchanged master geometry into each tile.
- Put registration/cut marks, row-column IDs, garment/revision, and a page map in safe areas. Ensure notches, labels, and every piece remain covered across the union of tiles. Show how to trim and align the overlap.
- Include a dedicated calibration page with a 100 × 100 mm square, horizontal/vertical checks, and printing instructions. Reuse those checks on the map or other sheets where practical.

### A0 plotter printing

- Page size: 841 × 1189 mm, or its landscape rotation; default 10 mm margins.
- Rotate/translate pieces to fit without scaling. Use additional A0 sheets for separate pieces. When one piece exceeds the usable sheet size, split it across A0 sheets with a 10 mm overlap and registration marks; identify the split on the page map.
- Include the same garment revision and calibration checks. Describe any alternative custom roll size explicitly rather than silently replacing A0.

## Verification and release

For a reusable A4 printer test, run `python scripts/print_calibration.py <output-folder>` from the skill folder. It creates a vector SVG/PDF with the same coordinates and checks page size, square geometry, and PDF print preference. The tool is a calibration test, not a drafting engine or proof of a garment's fit. It uses ReportLab and pypdf from the available document runtime.

Digital checks:

- Confirm physical SVG dimensions and viewBox agree in both axes.
- Check the 100 mm square is 100 mm in SVG and `100 × 72 / 25.4` PDF points in both directions. Check a longer known horizontal/vertical distance and one assembled seam across tile boundaries.
- Verify full geometry coverage across tiles, matching overlap marks, page sizes, and absence of unintended scale/stretch transforms. Inspect all rendered pages for readability/clipping and confirm pattern paths remain vectors.
- Record digital results with the garment/revision. Mark unresolved checks explicitly.

Physical checks:

- Print the calibration page using **Actual Size / 100%**, with matching paper size. Disable Fit, Shrink, driver resizing, and borderless enlargement. For pre-tiled PDFs, do not tile them again.
- For a large master PDF printed using Acrobat Poster, set **Tile Scale 100%** and use overlap/cut marks. [Adobe large-document printing](https://helpx.adobe.com/acrobat/desktop/print-documents/set-up-and-print-pdfs/large-documents.html)
- Measure both sides of the square with a ruler. Default acceptance is 99.5–100.5 mm in each axis. Check a longer line or assembled tile join before printing/cutting the complete set.
- If either direction fails, stop and resolve paper/driver/viewer settings; reprint the test. Do not compensate by guessing a garment scale or assuming horizontal and vertical error match.
- Record measured dimensions, printer, paper, and date before marking physical scale checked. An actual toile/fitting is the separate fit check.
