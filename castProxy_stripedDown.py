#!/usr/bin/env python3
"""
  castProxy.py: Luis Pereia approach to CastLabs's python programming task https://github.com/castlabs/python_programming_task
  Note: striped down version without logging and less comments!
  upstream server: https://postman-echo.com or my own
  Libraries documentation:
	  http.server -> https://docs.python.org/3/library/http.server.html
	  pyjwt that follows the  industry-standard RFC7519 (install via pip3) -> https://pyjwt.readthedocs.io/en/latest/
	  requests -> https://requests.readthedocs.io/en/master/
      + datetime, time
"""
__author__ = "Luis Pereira"
__version__ = "1.0.0"
__email__ = "pereira@lpspot.com"

import jwt, datetime, time, requests
from http.server import BaseHTTPRequestHandler, HTTPServer

def genJwtHeader(user='username', date=str(datetime.date.today())):
    jwtSecret = '0xa9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf'
    iat = datetime.datetime.utcnow() #Issued At
    jti = str(int(time.time()*4545)) #nonce. unique, therefore incremental
    msg = { 'iat': iat, 'jti':jti,'user':user,'date':date }
    jwtEncoded = jwt.encode(msg, jwtSecret, algorithm='HS512')
    return {'x-my-jwt': jwtEncoded }

class handler(BaseHTTPRequestHandler):
    def forward(self, type):
        fwUrl = "http://postman-echo.com/" + type.lower()
        newHeaders = {}
        for key in self.headers:
            if (key != 'Content-Length' and key != 'Host'):
                newHeaders[key] = self.headers[key]
        if type.lower() == 'post': newHeaders = {**newHeaders, **genJwtHeader()}
        try:
            resp = requests.request(type.lower(), fwUrl, headers=newHeaders, verify=False)
        except requests.exceptions.RequestException as e:
            self.send_error(500)
            logging.error("Something went wrong requests Error: %s", e)
            raise SystemExit(e)
        if (resp.status_code >= 100 and resp.status_code < 300):
            self.send_response(resp.status_code)
            for key, value in resp.headers.items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(resp.content)
        elif (resp.status_code >= 300 and resp.status_code < 400): #Not allowing redirects!
            self.send_error(500)
        elif (resp.status_code >= 400 ):
            self.send_error(resp.status_code)

    def do_POST(self):
        self.forward('POST')
    def do_GET(self):
        self.forward('GET')
    def do_PUT(self):
        self.forward('PUT')

def runServer(host="localhost", port=81):
    webserver = HTTPServer((host, port), handler)
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass
    webserver.server_close()

if __name__ == '__main__':
    try:
        with runServer():
            while True:time.sleep(1)
    except KeyboardInterrupt:
        pass
