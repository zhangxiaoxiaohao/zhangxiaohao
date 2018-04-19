z = int(input("请输入第一个数字:"))
c = int(input("请用户输入第二个数字:"))
sum = 0
if z < c:
	for i in range(z,c+1):
		print(i)
		sum = sum+i
else:
	print("输入错误")

print(sum)
