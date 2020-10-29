from http.server import BaseHTTPRequestHandler
from datetime import datetime, timezone
import svgwrite


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/svg+xml')
        self.end_headers()
        dwg = svgwrite.Drawing(filename='sample.svg', size=("500px", "80px"))
        dwg.add(dwg.text(
            f"It is currently {datetime.now(tz=timezone.utc)}",
            insert=(5, 20),
            style='font: 600 18px "Segoe UI", Ubuntu, Sans-Serif; fill: #fe428e;'
        ))
        dwg.add(dwg.text(
            f"Thanks for visiting my Profile Page!",
            insert=(5, 50),
            style='font: 600 18px "Segoe UI", Ubuntu, Sans-Serif; fill: #fe428e;'
        ))
        self.wfile.write(dwg.tostring().encode())
        return
