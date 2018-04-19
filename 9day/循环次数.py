while True:
	z = int(input("请输入一个数字"))
	c = int(input("请输入一个数字"))
	sum = 0
	if z < c:
		for i in range(z,c+1):
			print(i)
			sum = sum+i
		print("请重新输入")
		break
	print(sum)
		
