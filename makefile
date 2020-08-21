##CastLabs jwt programing task make file
HTTP_PORT = 8080

help:
	@echo "####################################"
	@echo "# LP's implementation of CastLabs  #"
	@echo "# programing task (jwt proxy)      #"
	@echo "#                                  #"
	@echo "# Main availiable targets are:     #"
	@echo "#  - build                         #"
	@echo "#  - run                           #"
	@echo "#  - test                          #"
	@echo "####################################"

install-py-libs:
	pip install PyJWT
	pip install requests

run-py:
	python3 castProxy.py --log=info

run-py-debug:
	python3 castProxy.py --log=debug

build:
	@echo "Building the Docker image"
	docker build .
	@echo "Docker image built"

run:
	@echo "Docker run will run the service and map/pat the port $(HTTP_PORT)"
	docker run -d -p 0.0.0.0:$(HTTP_PORT):81/tcp jwtproxyprogramingtask_castproxy python3 castProxy.py --log=info
	@echo "Done"

composer-run:
	docker-compose up

test:
	curl -X POST 'http://localhost:8080/whatever' --header 'testOrig: something'
