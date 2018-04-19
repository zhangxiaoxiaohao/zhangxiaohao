account = "123456"
pwd = "123456"
money = 99999999999


a_acc = input("请输入账号")
a_pwd = input("请输入密码")

if a_acc == account and a_pwd ==pwd:
	a_money = float(input("请输入取款金额"))
	if money >= a_money:
		print("取了%.02f元,剩余5%.02f"%(a_money,money-a_money))
	else:
		print("账户余额不足")
else:
	print("账号登录错误")
