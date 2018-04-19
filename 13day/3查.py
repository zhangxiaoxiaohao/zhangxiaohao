print("名片系统".center(30,"*"))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("3:删除名片".center(30," "))
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
			print("修改")
	elif fun_number == 4:
			print("删除")
