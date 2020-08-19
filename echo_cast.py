#!/usr/bin/env python3
"""
  Luis Pereia echo server for the CastLabs's python programming task https://github.com/castlabs/python_programming_task.
"""
__author__ = "Luis Pereira"
__version__ = "1.0.0"
__email__ = "pereira@lpspot.com"

from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse, logging, jwt, json, datetime, requests, time

class handler(BaseHTTPRequestHandler):
	def reply(self, type):
		logging.info("New incomming %s from %s, requested path %s", type, self.address_string(), str(self.path))
		logging.debug("Path: %s\n== Headers ==\n%s\n", str(self.path), str(self.headers))
		self.protocol_version = 'HTTP/1.1'
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		resp={}
		resp["info"] = "this is just a HTTP echo server"
		resp["path"] = str(self.path)
		resp["headers"] = {}
		for key in self.headers:
			resp["headers"][key]=self.headers[key]		
		self.end_headers()
		resp = json.dumps(resp)
		self.wfile.write(resp.encode('utf-8'))
		logging.info("All done sent response send back to the client!")
		
	def do_POST(self):
		self.reply('post')
	def do_GET(self):
		self.reply(type='get')

def runServer(host="localhost", port=88):
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
