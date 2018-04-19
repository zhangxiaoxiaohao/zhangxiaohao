list = [1,5,50,80,40,60,10,70,4,99]
print(list)
for i in range(len(list)):
	for j in range(i+1,len(list)):
		if list[i]>list[j]:
			list[i],list[j] = list[j],list[i]
	print(list)
key = 4
center = int(len(list)/2)
if key in list:
	while True:
		if list[center] > key:
			center-=1
		elif list[center] < key:
			center += 1
		elif list[center] == key:
			print("4在%d位"%center)
			break
			
