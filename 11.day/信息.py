card = {"name":"张世豪","age":20,"sex":"男","group":"汉"}
print(card)
card["address"] = "河南"
card["se"] = "单身"
print(card)
card.pop("se")
print(card)
card["age"] = 21
print(card)
print(card.get("sex")) 
