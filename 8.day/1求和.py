i = 1
x = 0
y = 0
while i <=100:
    if i%2 ==0:
        x += i
    else:
        y += i
    i+=1
print("偶数:%d"%x)
print("奇数:%d"%y)
