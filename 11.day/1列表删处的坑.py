name = [1,2,3,4,5,6,7,8,9]
new_name = name[:]
for i in new_name:
	name.remove(i)
print(name)





s = [1,2,3,4,5,6,7,8]
for i in range(len(s)-1,-1,-1):
	s.pop(i)
print(s)
