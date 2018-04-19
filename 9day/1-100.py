for i in range(1,11):
	a = int(input("请输入你的数字1~100："))
	if a >100 and a <1:
		print("输入错误")
		break
	elif a == 55:
		print("回答正确")
		break
	elif a > 55:
		print("请在小一点")
		continue
	elif a < 55:
		print("请在大一点")
		continue
