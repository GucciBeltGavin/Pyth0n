# save this file as random_int.py
from random import randint
def ranint():
	r = randint(65,91)
	return r
	
def main():
	for r in range (1000000000000000):
		rint = ranint()
		print (rint,end="")
	
	
main()
