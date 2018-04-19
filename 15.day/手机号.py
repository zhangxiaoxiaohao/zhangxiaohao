def s_phone(phone):
	if phone.startswith("1") and len(phone)==11:
		return True
	else:
		return False
phone = input("请输入手机号")
seee = s_phone(phone)
if seee == False:
	print("手机号是错的")
else:
	print("输入正确")
phone2 = input("请输入手机号")
seee = s_phone(phone2)
if seee == False:
	print("手机号是错的")
else:
	print("输入正确")
