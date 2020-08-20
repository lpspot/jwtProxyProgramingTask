# LP approach to CastLabs JWT Proxy Programing Task
 My approach to maciejstromich's CastLabs JWT Proxy programming task https://github.com/castlabs/python_programming_task
 - Without Docker/Makefile

## Files:
 - castProxy.py --> The Programing Task itself;
    - Run: castProxy.py --log=[info|debug]
    - Usage: `curl -X POST 'http://localhost:81/whatever' --header 'testOrig: something'`
 - castProxy_stripedDown.py --> Striped-down version without logging and less comments;
 - echo_cast.py --> MyEcho server;
