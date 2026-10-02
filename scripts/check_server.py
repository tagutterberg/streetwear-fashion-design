"""Check localhost export validation, formats, and non-overwriting saves."""
import json
import tempfile
import threading
from functools import partial
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path
from serve_review import ReviewHandler, export_name, validate_svg


def check():
    svg = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 720"><rect width="400" height="720" fill="white"/></svg>'
    validate_svg(svg)
    for unsafe in (
        svg.replace(b'<rect', b'<script'),
        svg.replace(b'fill="white"', b'onload="alert(1)"'),
        svg.replace(b'fill="white"', b'fill="url(https://example.com/a)"'),
        svg.replace(b'400 720', b'0 720'),
        b'<!DOCTYPE svg>' + svg,
        svg.replace(b'<rect', b'<foreignObject'),
    ):
        try:
            validate_svg(unsafe)
        except ValueError:
            pass
        else:
            raise AssertionError('Unsafe SVG accepted')
    for name in ('../x.json', '/x.png', '.hidden.svg', 'x.html', 'x\\y.svg'):
        try:
            export_name(name)
        except ValueError:
            pass
        else:
            raise AssertionError(name)

    with tempfile.TemporaryDirectory(prefix='fashion-export-check-') as folder:
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(ReviewHandler, directory=folder))
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        host = f'127.0.0.1:{server.server_port}'

        def post(name, data, origin=None):
            conn = HTTPConnection('127.0.0.1', server.server_port, timeout=5)
            conn.request('POST', '/_export?name=' + name, data, {'Origin': origin or 'http://' + host, 'X-Review-Export': '1'})
            res = conn.getresponse()
            body = res.read()
            status = res.status
            conn.close()
            return status, body

        try:
            for kind in ('fashion-review-project', 'fashion-review-feedback', 'fashion-design-explorer-project', 'fashion-design-choices'):
                status, body = post(kind + '.json', json.dumps({'kind': kind, 'schemaVersion': 1}).encode())
                assert status == 200, body
            assert post('sketch.svg', svg)[0] == 200
            assert post('sketch.svg', svg)[0] == 200
            assert (Path(folder) / 'exports/sketch.svg').read_bytes() == svg
            assert (Path(folder) / 'exports/sketch-2.svg').read_bytes() == svg
            assert post('x.svg', svg.replace(b'fill="white"', b'onload="bad"'))[0] == 400
            assert post('x.json', b'{"kind":"unknown","schemaVersion":1}')[0] == 400
            assert post('x.json', b'[]')[0] == 400
            assert post('x.png', b'not a png')[0] == 400
            assert post('x.svg', svg, 'https://example.com')[0] == 403
        finally:
            server.shutdown()
            server.server_close()
            worker.join(timeout=5)
    print('PASS: safe SVG, supported JSON, bad inputs/origin rejected, existing files preserved.')


if __name__ == '__main__':
    check()
