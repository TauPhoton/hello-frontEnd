from time import sleep
from os import get_terminal_size as terminalsize

def run():
	x,y = terminalsize()
	for i in range(y-1):
		print("*"*(x-1))

if __name__ == "__main__":
	run()