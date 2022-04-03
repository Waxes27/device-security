config : setup
	sudo perl inxi -Mi --output json --output-file `pwd`/config/config.json
	-rm inxi*
	sudo python3 config/neat_yml.py

setup:
	wget https://raw.githubusercontent.com/smxi/inxi/master/inxi
	