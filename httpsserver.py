# openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
# You need to specify keyfile if the certificate does not contain the private key
# https://docs.python.org/3/library/ssl.html#combined-key-and-certificate

import http.server, ssl

print("Connecting")

server_address = ('0.0.0.0', 443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='localhost.pem',
                               keyfile='localhost.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()

print("Connected")