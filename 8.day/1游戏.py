x = random.randint(1,100)
b = 0
while b <= 10:
	z =int(input("请输入数字"))
	if z < x:
		print("你输入的数字偏小")
	elif z > x:
		print("你输入的数字偏大")
	elif z == x:
		print("恭喜你答对了")
		break
	b+=1
