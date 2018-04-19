card = [{"name":"张三","age":12},{"name":"李四","age":14},{"name":"王五","age":15}]
name = input("请输入名字")
s = 0
for temp in card:
	if name == temp["name"]:
		s = 1
		print(temp["name"],temp["age"])
		break
if s == 0:
	print("查无此人")
