FROM python:3.8.5-slim-buster
RUN pip install PyJWT
RUN pip install requests
#RUN pip install -r requirements.txt #replaces the two lines above
RUN mkdir /usr/src/jwtproxy
WORKDIR /usr/src/jwtproxy
EXPOSE 81
COPY . .
#ENTRYPOINT ["python3", "./castProxy.py", "--log=info"]
