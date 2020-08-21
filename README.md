# LP approach to CastLabs JWT Proxy Programing Task
 My approach to maciejstromich's CastLabs JWT Proxy programming task https://github.com/castlabs/python_programming_task

## Files:
 - castProxy.py --> The Programing Task itself;
    - Run: castProxy.py --log=[info|debug]
    - Usage: `curl -X POST 'http://localhost:81/whatever' --header 'testOrig: something'`
 - castProxy_stripedDown.py --> Striped-down version without logging and less comments;
 - echo_cast.py --> MyEcho server;
 - Dockerfile --> Docker file based on the python:3.8.5-slim-buster image, installs the required libraries
	- Build: docker build .
	- Run: docker run -d -p 0.0.0.0:$(HTTP_PORT):81/tcp jwtproxyprogramingtask_castproxy python3 castProxy.py --log=info
 - docker-compose.yml --> composer v3 file, runs the proxy and maps the port docker host port 8080 to itself
	- Run: docker-compose up
 - makefile
	- Main targets: `buil`, `run` (docker run) and `test`
    - Also available:  install-py-libs, run-py, run-py-debug
 