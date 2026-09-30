"""Serve a local review and save browser exports inside its exports folder."""
import argparse
import json
import re
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit


def export_name(value):
    if not re.fullmatch(r'[\w.-]{1,180}\.(?:json|png)', value) or value.startswith('.'):
        raise ValueError('Invalid export filename')
    return value


class ReviewHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        route = urlsplit(self.path)
        origin = self.headers.get('Origin')
        host = f'127.0.0.1:{self.server.server_port}'
        if route.path != '/_export' or self.headers.get('Host') != host or origin != 'http://' + host or self.headers.get('X-Review-Export') != '1':
            self.send_error(403)
            return
        try:
            name = export_name(parse_qs(route.query).get('name', [''])[0])
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 60000000: raise ValueError('Export exceeds size limit')
            data = self.rfile.read(length)
            if len(data) != length: raise ValueError('Incomplete export')
            if name.endswith('.png'):
                if not data.startswith(b'\x89PNG\r\n\x1a\n'): raise ValueError('Invalid PNG')
            else:
                value = json.loads(data)
                if value.get('kind') not in ('fashion-review-project', 'fashion-review-feedback') or value.get('schemaVersion') != 1: raise ValueError('Invalid review JSON')
            root = Path(self.directory).resolve()
            folder = (root / 'exports').resolve()
            if folder.parent != root: raise ValueError('Invalid export directory')
            folder.mkdir(exist_ok=True)
            dest = folder / name
            number = 1
            while True:
                try:
                    with dest.open('xb') as out: out.write(data)
                    break
                except FileExistsError:
                    number += 1
                    dest = folder / f'{Path(name).stem}-{number}{Path(name).suffix}'
            result = json.dumps({'url':'/exports/' + dest.name}, ensure_ascii=True).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(result)))
            self.end_headers()
            self.wfile.write(result)
        except (ValueError, AttributeError, OSError) as error:
            self.send_error(400, str(error))


if __name__ == '__main__':
    for bad in ('../x.json', '/x.png', '.hidden.json', 'x.html', 'x\\y.json'):
        try: export_name(bad)
        except ValueError: pass
        else: raise AssertionError(bad)
    assert export_name('gown-v2-prosjekt.json') == 'gown-v2-prosjekt.json'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--port', type=int, default=8766)
    args = parser.parse_args()
    root = args.directory.resolve(strict=True)
    if not root.is_dir(): parser.error('directory must be a folder')
    server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(ReviewHandler, directory=str(root)))
    print(f'Review: http://127.0.0.1:{args.port}/skisseverksted.html', flush=True)
    server.serve_forever()
