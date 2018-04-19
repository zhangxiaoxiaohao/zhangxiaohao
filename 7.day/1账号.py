hao = "xiaoxiaohao"
mi = "123456"

a_hao =input("请输入账号")
p_mi =input("请输入密码")
if a_hao == hao and p_mi == mi:
    print("登录成功")
    #0---adc('鲁班大师')
    #1---肉('程咬金')
    #3---法师('王昭君')
    choose_hero= int(input("请输入:0---adc'鲁班大师' 1---肉'程咬金' 3---法师'王昭君'"))
    if choose_hero == 0:
       print("鲁班大师")
    elif choose_hero == 1:
       print("程咬金")
    elif choose_hero == 3:
       print("dsadas") 
else:
    pass
    #if hao mi == 3:
       print("密码记错了")
