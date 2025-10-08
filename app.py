from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from controllers.user_controller import list_users, store_user
from views import render_template

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            html = list_users()
            self._send_html(html)

        elif path == "/add_user":
            html = render_template("add_user.html")
            self._send_html(html)

    def do_POST(self):
        path = urlparse(self.path).path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = parse_qs(post_data.decode())

        if path == "/store_user":
            store_user(data)
            self._redirect("/")

    def _send_html(self, html):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def _redirect(self, location):
        self.send_response(302)
        self.send_header("Location", location)
        self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), MyHandler)
    print("Server running at http://localhost:8080")
    server.serve_forever()
