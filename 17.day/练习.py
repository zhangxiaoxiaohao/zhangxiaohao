for i in range(1,10):
	for j in range(1,i+1):
		x = i*j
		print("%d*%d=%d\t"%(j,i,x),end=(" "))
	print("")

for s in range(1,10):
	for j in range(1,s+1):
		x=s*j
		print("%d*%d=%d"%(j,s,x),end=(" "))
	print("")

for z in range(1,10):
	for j in range(1,z+1):
		a = z*j
		print("%d*%d=%d"%(j,z,a),end=(" "))
	print(" ")	

for x in range(1,10):
	for j in range(1,x+1):
		a = x*j
		print("%d*%d=%d"%(j,x,a),end=(" "))
	print(" ")

for q in range(1,10):
	for j in range(1,q+1):
		a = q*j
		print("%d*%d=%d"%(j,q,a),end=(" "))
	print(" ")

for c in range(1,10):
	for j in range(1,c+1):
		a = c*j
		print("%d*%d=%d"%(j,c,a),end=(" "))
	print(" ")



for z in range(1,10):
	for j in range(1,z+1):
		a = z*j
		print("%d*%d=%d"%(j,z,a),end=(" "))
	print(" ")



x = int(input("请输入年份"))
if (x%4==0 and x%100!=0) or (x%400==0):
	print("闰年")
else:
	print("平年")

def name(x):
	if (x%4==0 and x%100!=0) or (x%400==0):
		print("闰年")
	else:
		print("平年")
x = int(input("请输入年份"))
name(x)






















