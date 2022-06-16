from http.server import HTTPServer,SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('192.168.0.88', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    
run()