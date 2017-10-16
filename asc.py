#save file as asc.py
def asc2():
	for i in range(256):
		c = chr(i)
		print("[",i,"=",c,"]")
		if (i % 16 == 0):
			print("\n")
def main():
	asc2()
	
main()
