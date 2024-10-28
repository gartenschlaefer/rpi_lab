# --
# makefile i2c

# name of main file
main_file_name = "main"

# general
all: build

# build
build:
	rshell -p /dev/ttyACM0 cp /world/dekutree/git/rpi_lab/i2c/main.py /pyboard/

# serial communication
com:
	minicom -D /dev/ttyACM0