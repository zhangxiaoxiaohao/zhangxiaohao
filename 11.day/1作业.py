list1=[]

listName=[]
ints=3
while ints>0:
	dict = {}
	name = input("请输入姓名:")
	if name in listName:
		print("姓名重复，请重新输入:")
		continue;
	listName.append(name)
	age = int(input("请输入年龄："))
	sex = input("请输入性别：")
	qq = input("请输入QQ：")
	tizhong = input("请输入体重：")
	dict["name"] = name
	dict["sex"] = sex
	dict["age"] = age
	dict["qq"] = qq
	dict["tizhong"] = tizhong
	list1.append(dict)
	ints=ints-1;
age_sum =0
for i in list1:
	age_sum = age_sum+i.get("age")
	print(i)
print("年龄平均是%0.2f"%(age_sum/len(list1)))
