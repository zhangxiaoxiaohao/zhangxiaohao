height = int(input("请输入身高"))
money = int(input("请输入身价"))
face = int(input("请输入颜值"))
if height >=180 and money >10000000 and face >=99:
    print("高富帅")
elif height <175 and money >10000000 and face >=99:
    print("富帅")
elif face >=99:
    print("帅")
elif height <=160 and moeny <100 and face <60:
    print("渣渣")
