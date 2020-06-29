



f = open("myfile.bin", "w")
index = 0


for i in range(4194304):
	f.write(0)
	f.write(1)
f.close()

