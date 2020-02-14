all: simple_gamble.pdf change_in_utility.pdf utility.pdf simple_gamble_incesto_free_rider.pdf

remake: clear_all all

simple_gamble_incesto_free_rider.pdf:
	/usr/bin/python3 simple_gamble_incesto_free_rider.py

simple_gamble_incesto.pdf:
	/usr/bin/python3 simple_gamble_incesto.py

simple_gamble.pdf:
	/usr/bin/python3 simple_gamble.py

change_in_utility.pdf:
	/usr/bin/python3 change_in_utility.py

utility.pdf:
	/usr/bin/python3 utility.py

clear_all: 
	rm *.pdf
	rm *.png


