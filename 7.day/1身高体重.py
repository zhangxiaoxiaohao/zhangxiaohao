height = float(input("请输入身高(m)"))
weight = float(input("请输入体重(公斤)"))
bmi = weight/height**2
if bmi < 18.5:
	print("廋成狗")
elif bmi >= 18.5 and bmi < 25:
	print("正常")
elif bmi >= 25 and bmi < 28:
	print("过重")
elif bmi >= 28 and bmi < 32:
	print("肥胖")
elif bmi > 32:
	print("胖成猪")
print(bmi)
