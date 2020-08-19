# LP approach to CastLabs JWT Proxy Programing Task
 My approach to maciejstromich's CastLabs JWT Proxy programming task https://github.com/castlabs/python_programming_task
 - Without Docker/Makefile

## Files:
 - castProxy.py --> The Programing Task itself;
    - Run: castProxy.py --log=[info|debug]
    - Usage: `curl --location --request POST 'http://localhost:81/whatever' \
--header 'testOrig: something' \
--header 'Content-Type: application/json' \
--header 'Cookie: sails.sid=s%3AgR-R6X29Bi-woE0LYlBRQAGzQ6J7YfJo.own%2FL1MeN9EbVj8rBIXpTTpQd3wOtR2qOVucTNcKUZM' \
--data-raw '{'\''originalBodyData'\'':'\''payload'\''}'`
 - castProxy_stripedDown.py --> Striped-down version without logging and less comments;
 - echo_cast.py --> MyEcho server;
