.PHONY: clean

clean:
	rm -f generated_code

run-client:
	python3 client.py
	
run-server:
	python3 server.py

lint:
	python3 -m flake8