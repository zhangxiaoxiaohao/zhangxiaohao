def a_num(num):
	if num ==1:
		return 1
	else:
		return num*a_num(num-1)
print(a_num(5))
