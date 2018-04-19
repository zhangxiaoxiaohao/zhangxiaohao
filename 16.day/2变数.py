num = [1,2]
def a():
	global num
	num = 3
	print(num)
a()
print(num)
