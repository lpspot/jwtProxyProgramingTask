# LP approach to CastLabs JWT Proxy Programing Task
 My approach to maciejstromich's CastLabs JWT Proxy programming task https://github.com/castlabs/python_programming_task
 - Makefile to be added later

## Files:
 - castProxy.py --> The Programing Task itself;
    - Run: castProxy.py --log=[info|debug]
    - Usage: `curl -X POST 'http://localhost:81/whatever' --header 'testOrig: something'`
 - castProxy_stripedDown.py --> Striped-down version without logging and less comments;
 - echo_cast.py --> MyEcho server;
 - Dockerfile --> Docker file based on the python:3.8.5-slim-buster image, installs the required libraries
	- Build: docker build .
	- Run: docker run -d -p 0.0.0.0:8080:81/tcp e3d57b8569da python3 /usr/src/jwtproxy/castProxy.py --log=info
 - docker-compose.yml --> composer v3 file, runs the proxy and maps the port docker host port 8080 to itself
	- Run: docker-compose up