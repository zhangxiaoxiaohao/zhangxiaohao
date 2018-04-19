kk = int(input("请输入年份"))
if (kk%4 == 0 and kk%100 == 0 and kk%400 == 0):
    print("闰年")
else:
    print("平年")
