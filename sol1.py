
f = open("monfichier.txt", "w+")

for x in range(2,31):
	f.write("Table de multiplication par %d\n" % x)
	for y in range(1,21):
		f.write("{} fois {} = {}\n".format(x, y, x*y))

print("fin")

