from http.server import BaseHTTPRequestHandler
from datetime import datetime, timezone
import svgwrite


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/svg+xml')
        self.end_headers()
        dwg = svgwrite.Drawing(filename='sample.svg', size=("850px", "100px"))
        dwg.add(dwg.text(
            f"It is currently {datetime.now(tz=timezone.utc)}",
            insert=(5, 20),
            style='font: 600 18px "Segoe UI", Ubuntu, Sans-Serif; fill: #fe428e;'
        ))
        dwg.add(dwg.text(
            f"Thanks for visiting my Profile Page",
            insert=(5, 50),
            style='font: 600 18px "Segoe UI", Ubuntu, Sans-Serif; fill: #fe428e;'
        ))
        #message = f'<svg width="850" height="100" fill="none" xmlns="http://www.w3.org/2000/svg"><style>.header {{font: 600 18px "Segoe UI", Ubuntu, Sans-Serif; fill: #fe428e; animation: fadeInAnimation 0.8s ease-in-out forwards;\}}</style><text class="header" x="5" y="20">Hello.. it is now {datetime.now(tz=timezone.utc)}</text><text class="header" x="5" y="50">Thank you very much for visiting my Github profile.</text></svg>'
        self.wfile.write(dwg.tostring().encode())
        return
