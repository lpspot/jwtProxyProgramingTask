##CastLabs jwt programing task make file

help:
	@echo "####################################"
	@echo "# LP's implementation of CastLabs  #"
	@echo "# programing task (jwt proxy)      #"
	@echo "#                                  #"
	@echo "# Availiable targets are:          #"
	@echo "#  - run:   runs the app           #"
	@echo "#  - debug: runs the app with  the #"
	@echo "#           loglevel set to debug  #"
	@echo "#                                  #"
	@echo "####################################"

run:	
	pip install PyJWT
	pip install requests
	python3 castProxy.py --log=info HTTP_PORT

debug:
	pip install PyJWT
	pip install requests
	python3 castProxy.py --log=debug
