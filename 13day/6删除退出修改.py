print("名片系统".center(30,"*"))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:退出系统".center(30," "))
cards = []
while True:
	fun_number = int(input("请选择功能"))
	if fun_number ==1:
		print("新增")
		flag = 0
		card={}
		name = input("请输入名字")
		for temp in card:
			if name == temp["name"]:
				flag = 1
				break
		if flag == 1:
			print("名字重复")
			continue
		jop = input("请输入职位")
		phone = int(input("请输入手机号"))
		company = input("请输入公司名字")
		address = input("请输入公司地址")
		card["name"] = name
		card["jop"] = jop
		card["phone"] = phone
		card["company"] = company
		card["address"] = address
		cards.append(card)
		print("新增成功")
	elif fun_number == 2:
		name = input("请输入要查的姓名")
		flag = 0
		count = 0
		for temp in cards:
			count+=1
			if name == temp["name"]:
				flag = 1
				break
		if flag == 0:
			print("查无此人\n")
		else:
			print("姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n地址:%s"%(cards[count-1]["name"],cards[count-1]["jop"],cards[count-1]["phone"],cards[count-1]["company"],cards[count-1]["address"]))
	elif fun_number == 3:
		name = input("你要修改的名字")
		for temp in cards:
			if name == temp["name"]:
				print("1:修改名字".center(30,"*"))
				print("2:修改职位".center(30,"*"))
				print("3:修改手机号".center(30,"*"))
				print("4:修改公司名称".center(30,"*"))
				print("5:修改公司地址".center(30,"*"))
				change_num = int(input("选择修改的序列号"))
				if change_num == 1:
					name = input("请输入新的名字")
					temp["name"] = name
				elif change_num == 2:
					jop = input("请输入新的职位")
					temp["jop"] = jop
				elif change_num == 3:
					phone = int(input("请输入新的手机号"))
					temp["phone"] = phone
				elif change_num == 4:
					company = input("请输入新的公司")
					temp["company"] = company
				elif change_num == 5:
					address = input("请输入新的公司地址")
					temp["address"] = address
				else:
					print("输入错误\n")
	elif fun_number == 4:
		name = input("请输入要删除的内容")
		s = 0
		x = 0
		for op in cards:
			x+=1
			if name == op["name"]:
				s = 1
				a = int(input("确认删除吗:0__删除 1__返回"))
				if a == 0:
					print("删除成功")
					cards.remove(op)
				else:
					print("返回菜单")
			else:
				print("输入错误")
				break
	elif fun_number == 5:
		
		print("退出程序")
		break
