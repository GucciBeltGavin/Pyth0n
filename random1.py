from random import randint
def randlist(r,usedlist,done):
	alpha = ["a", "b", "c", "d", "e", "f"]
	usedlist[r] = 1
	c = alpha[r]
	sum = 0
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
	done = True
	return c,usedlist,done
	
def main():
	used = [0, 0, 0, 0, 0, 0]
	while True:
		r = randint(0, 5)
		done = 0
		c = randlist(r,used,done)
		print(used)
main()
