#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            message = ""
            message += "<html><body>Hello!</body></html>"
            self.wfile.write(message.encode())
            print(message)
            return
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        port = 8000
        httpd = HTTPServer(('', port), WebServerHandler)
        print("Web Server running on port %s" % port)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("^C entered, stopping web server....")
        httpd.socket.close()


if __name__ == '__main__':
    main()
