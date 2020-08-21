#!/usr/bin/env python3
"""
  castProxy.py: Luis Pereia approach to CastLabs's python programming task https://github.com/castlabs/python_programming_task.
  Note: As the task was to "build an HTTP proxy" I used two libraries to "HTTPServer" and "BaseHTTPRequestHandler" to handle the requests (http server)
        and "requests" as client to perform the upstream http requests. Otherwise the python proxy library could be used https://pypi.org/project/proxy.py/
  upstream server: https://postman-echo.com or myEcho http://localhost:88/
  Libraries documentation:
	  http.server -> https://docs.python.org/3/library/http.server.html
	  pyjwt that follows the  industry-standard RFC7519 (install via pip3) -> https://pyjwt.readthedocs.io/en/latest/
	  requests -> https://requests.readthedocs.io/en/master/
      + argparse, logging, datetime, time
"""
__author__ = "Luis Pereira"
__version__ = "1.0.0"
__email__ = "pereira@lpspot.com"

import argparse, logging, jwt, datetime, time, requests
from http.server import BaseHTTPRequestHandler, HTTPServer

def genJwtHeader(user='username', date=str(datetime.date.today())):
    jwtSecret = '0xa9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf' #????????
    logging.info('Generating the JWT')
    iat = datetime.datetime.utcnow() #Issued At
    jti = str(int(time.time()*4545)) #nonce. unique, therefore incremental
    msg = { 'iat': iat, 'jti':jti,'user':user,'date':date }
    jwtEncoded = jwt.encode(msg, jwtSecret, algorithm='HS512')
    logging.debug('JWT Header: %s', jwtEncoded )
    return { 'x-my-jwt': jwtEncoded }
    #jwtDecoded=myJwt.decode(jwtEncoded, jwtSecret, algorithm='HS512')

class handler(BaseHTTPRequestHandler):
    def forward(self, type):
        echoServer = { "postman":"http://postman-echo.com/", "lp":"http://localhost:88/" , "reqres":"https://reqres.in/api/login"}
        fwUrl = echoServer['postman'] + type.lower()
        logging.info("New incomming %s from %s, requested path %s", type, self.address_string(), str(self.path))
        logging.debug("Path: %s\n== Headers ==\n%s\n", str(self.path), str(self.headers))
        newHeaders = {}
        for key in self.headers:
            if (key != 'Content-Length' and key != 'Host'):
                newHeaders[key] = self.headers[key]
        if type.lower() == 'post': newHeaders = {**newHeaders, **genJwtHeader()}
        logging.info("Forwarding %s to url: %s", type, fwUrl)
        logging.debug("Headers: %s", newHeaders)
        try:
            resp = requests.request(type.lower(), fwUrl, headers=newHeaders, verify=False)
        except requests.exceptions.RequestException as e:
            self.send_error(500)
            #self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
            logging.error("Something went wrong requests Error: %s", e)
            raise SystemExit(e)
        if (resp.status_code >= 100 and resp.status_code < 300):
            logging.info("Response code: %s", resp.status_code)
            logging.debug("Response content: %s\nResponse Headers: %s", resp.content, resp.headers)
            self.send_response(resp.status_code)
            for key, value in resp.headers.items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(resp.content)
            logging.info("All done sent response send back to the client!")
        elif (resp.status_code >= 300 and resp.status_code < 400): #Not allowing redirects!
            self.send_error(500)
            logging.info("Redirect code %s received from the upstream server, Blocked!", resp.status_code)
        elif (resp.status_code >= 400 ):
            self.send_error(resp.status_code)
            logging.info("Error %s, forward back to the client", resp.status_code)

    def do_POST(self):
        self.forward('POST')
    def do_GET(self):
        self.forward('GET')
    def do_PUT(self):
        self.forward('PUT')

def runServer(host="0.0.0.0", port=81):
    logging.info('HTTP Server on %s:%s', host, str(port))
    webserver = HTTPServer((host, port), handler)
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass
    logging.info('Stopping the HTTP Server')
    webserver.server_close()

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("--log")
    args = p.parse_args()
    logLevel = args.log
    selLogLevel = getattr(logging, logLevel.upper(), None)
    logging.basicConfig(level=selLogLevel)
    try:
        with runServer():
            while True:time.sleep(1)
    except KeyboardInterrupt:
        pass
