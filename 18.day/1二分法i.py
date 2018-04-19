list = [2,4,6,8,10,12,14,16,18,20,22,24,26,]
key = 20

center = int(len(list)/2)
if key in list:

	while True:

		if list[center] > key:
			center = center - 1
		elif list[center] < key:
			center = center + 1
		elif list[center] == key:
			print("你要找的数字是%d在索引是%d"%(key,center))
			break
else:
	print("你要找的数字没")
