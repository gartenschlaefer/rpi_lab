# --
# makefile rpi

# name of main file
board_name = "pyboard"
main_file_name = "main.py"
device = "/dev/ttyACM0"

# --
# make rules

# general
all: build

# build
build:
	rshell -p $(device) cp ./$(main_file_name) /$(board_name)/

# read main file
read:
	rshell -p $(device) cat /$(board_name)/$(main_file_name)

# communicate
com:
	minicom -D $(device)