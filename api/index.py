from http.server import BaseHTTPRequestHandler
from cowpy import cow

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = cow.Cowacter().milk(f'Hello {self.headers["x-real-ip"]}! You are using {self.headers["User-Agent"]}. Thank you very much for visiting my Github profile.')
        self.wfile.write(message.encode())
        return
