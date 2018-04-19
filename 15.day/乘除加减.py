def aaa(x,y,l):
if l == "+":
		 = x+y
		return s
	elif l == "-":
		s = x-y
		return s
	elif l == "*":
		s = x*y
		return s
	elif l == "/":
		if y != 0:
			s = x/y
		else:
			return "输入错误"
	return s
while True:
	x =int(input("请输入数字"))
	y =int(input("请在输入一个数字"))
	s =input("+,-,*,/")
	sss = aaa(x,y,s)
	print(sss)
		
