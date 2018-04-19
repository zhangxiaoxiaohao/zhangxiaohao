s_account = "xiaoxiao"
s_pwd = "123456"
count = 1 #
while True:
	account = input("请输入账号")
	pwd = input("请输入密码")
	if account == s_account and pwd ==s_pwd:
		choose_hero = int(input("0-adc 1-肉 2-法"))
		if choose_hero == 0:
			print("鲁班大师")
		elif choose_hero == 1:
			print("程咬金")
		elif choose_hero == 2:

		break
	else:
		print("error%d次"%count)
		count+=1
		if count == 4:
			print("账号被封")
			break
