import time
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        fname = "index.html"
        HtmlFile = open(fname, 'r', encoding='utf-8')
        file = HtmlFile.read()

    def do_GET(self):
        # Respond to a GET request.
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        fname = "index.html"
        HtmlFile = open(fname, 'r', encoding='utf-8')
        file = HtmlFile.read()

        #print(file)
        #file = "hello world!"

        self.wfile.write(bytes(file,"utf8"))

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('10.0.0.9', 8080)
  httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
