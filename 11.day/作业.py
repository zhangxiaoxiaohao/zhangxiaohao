list = []
name_list=[]
count = 0
while True:
	if count == 3:
			break
	dict = {}
	name = input("名字")
	age = int(input("年龄"))
	sex = input("性别")
	qq = int(input("qq"))
	weiget = float(input("体重"))
	if name not in name_list:
		dict["name"] = name
		dict["age"] = age
		dict["sex"] = sex
		dict["qq"] = qq
		dict["weiget"] = weiget
		list.append(dict)
		name_list.append(name)
		print(list)
		count+=1
	else:
		print("名字重复")
age_sum =0
for i in list:
	age_sum = age_sum+i.get("age")
	print(i)
print("年龄的平均值是%0.2f"%(age_sum/len(list)))
