def aaa(x,y,l):
	if l == "+":
		s = x+y
		print("和是%.02f"%s)
	elif l == "-":
		s = x-y
		print("减是%.02f"%s)
	elif l == "*":
		s = x*y
		print("乘是%.02f"%s)
	elif l == "/":
		if y != 0:
			s = x/y
			print("除是%.02f"%s)
	else:
		print("输入错误")
while True:
	x =int(input("请输入数字"))
	y =int(input("请在输入一个数字"))
	s =input("+,-,*,/")
	aaa(x,y,s)
		
