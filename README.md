# LP approach to CastLabs JWT Proxy Programing Task
 My solution to maciejstromich's CastLabs JWT Proxy programming task https://github.com/castlabs/python_programming_task

## Files and usage

### Makefile
 - Main targets:
   - buil: `make build`
   - run: `make run`
   - test: `make test`
 - Also available:
   - `make [install-py-libs|run-py|run-py-debug]`
 
### Python
 - castProxy.py --> The Programing Task itself;
    - Run: `python3 castProxy.py --log=[info|debug]`
    - Test: `curl -X POST 'http://localhost:81/whatever' --header 'testOrig: something'`
 - castProxy_stripedDown.py --> Striped-down version without logging and less comments;
 - echo_cast.py --> Echo server;
    - Run: `python3 echo_cast.py`

### Docker
 - Dockerfile --> Docker file based on the python:3.8.5-slim-buster image, + installs the required libraries;
   - Build: `docker build -t jwtproxyprogramingtask_castproxy .`
   - Run: `docker run -d -p 0.0.0.0:$(HTTP_PORT):81/tcp jwtproxyprogramingtask_castproxy python3 castProxy.py --log=info`
 - docker-compose.yml --> composer v3 file, runs the proxy and maps the host port 8080 to it;
   - Run: `docker-compose up`
