def a():
	for i in range(1,20):
		name = input("请输入要注册的账号")
		print("注册账号成功")
		pwd = input("请输入要注册的密码")
		print("注册密码成功")
		name1 = input("请输入要登录的账号")
		pwd1 = input("请输入密码")
		b = input("是否登录1:是 2:否")
		
		if (b == 1) or (name1 == name and pwd1 == pwd):
			print("登录成功")
		elif b == 2:
			print("不登录")
		else:
			print("输入有误,请重新输入")
			continue
		name2 = input("请输入要注册的账号")
		if name2 == name:
			print("注册失败,账号已存在")
			continue
		pwd2 = input("请输入密码")
		if name2 != name:
			print("账号注册成功")
		name3 = input("请输入要登录的账号")
	
		a = int(print("是否登录1:是 2:否"))
		if (a == 1) or (name3 == name1):
			print("正在登录")
		elif (a == 1) or ("name3 != name1"):
			print("登录成功")
		else:
			print("登录失败")

		break




a()






