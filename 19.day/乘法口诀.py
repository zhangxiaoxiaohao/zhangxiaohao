def a():
	for i in range(1,10):
		for j in range(1,i+1):
			a = i*j
			print("%d*%d=%d"%(j,i,a),end=(" "))
		print(" ")
a()
