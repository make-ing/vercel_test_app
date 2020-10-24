from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','image/svg+xml')
        self.end_headers()
        message = f'<svg><text x="5" y="5">Hello {self.headers["x-real-ip"]}! You are using {self.headers["User-Agent"]}. Thank you very much for visiting my Github profile.</text></svg>'
        self.wfile.write(message.encode())
        return
