import http.server
import socketserver
import ssl

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("10.0.0.5", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
    httpd.serve_forever()
