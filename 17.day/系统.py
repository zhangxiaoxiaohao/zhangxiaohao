list = []
def interface():
	print("保安系统版本".center(28,"*"))
	print("1:新加入的人".center(30," "))
	print("2:查找人名".center(30," "))
	print("3:修改人名".center(30," "))
	print("4:退回的人".center(30," "))
	print("5:全部人名".center(30," "))
	print("6:退出系统".center(30," "))
def xxx():
	while True:
		fun_num = int(input("请选择功能"))
		if fun_num ==1:
			a_num()
		elif fun_num ==2:
			b_bbb()
		elif fun_num ==3:
			c_ccc()
		elif fun_num ==4:
			d_ddd()
		elif fun_num ==5:
			e_eee()
		elif fun_num ==6:
			print("退出系统")
			break
def a_num():
	while True:
		dict = {}
		name = input("请输入名字")
		sex = input("请输入性别")
		if sex !="男" and sex !="女":
			print("输入有误,请输入男或女")
			continue
		height = int(input("请输入身高"))
		if height >= 160:
			print("身高够了")
		elif height < 160: 
			print("身高不够")
			break
		else:
			print("输入错误")
			continue
		def qq_hua():
			if hua.startswith("1") and len(hua) == 11:
				return True
			else:
				return False
		hua = input("请输入你的电话号码")
		cheak = qq_hua()
		if cheak == False:
			print("输入错误")
			continue
		dict["name"]=name	
		dict["sex"]= sex
		dict["height"]=height
		dict["hua"]=hua
		list.append(dict)
		print("恭喜你入围成功\n")
		break
def b_bbb():
	name = input("请输入名字")
	flag = False
	for temp in list:
		if name == temp["name"]:
			flag = True
			print("已经成功并通过")
			print(" ")
			break
	if flag == False:
		print("还没报名")
def c_ccc():
	name = input("请输入要修改的名字")
	for temp in list:
		if name == temp["name"]:
			print("1:修改名字".center(30," "))
			print("2:修改性别".center(30," "))
			print("3:修改身高".center(30," "))
			print("4:修改手机号".center(30," "))
			ww_nume = int(input("请选择修改序号"))
			if ww_nume == 1:
				name = input("请输入新的名字")
				temp["name"] = name
			elif ww_nume == 2:
				sex = input("请输入新的性别")
				temp["sex"] = sex
			elif ww_nume == 3:
				height = input("请输入新的身高")
				temp["height"] = height
			elif ww_nume == 4:
				hao = input("请输入新的手机号")
				temp["hao"] = hao
def d_ddd():
	name = input("请输入要删除的名字")
	flag = 0
	for temp in list:
		if name == temp["name"]:
			flag = 1
			fff = int(input("确定要删除吗1:确定 2:返回"))
			if fff == 1:
				list.remove(temp)
				print("删除成功")
			break
	if flag == 0:
		print("没有此人")
def e_eee():
	for temp in list:
		for i in temp:
			print('%s:%s'%(i,temp[i]))

interface()
xxx()

