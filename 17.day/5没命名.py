fun = lambda a,b:a+b
print(fun(2,2))


fun = lambda a,b=5:a+b
print(fun(5,8))


def name(a,b,fun):
	print(fun(a,b))
name(1,7,lambda a,b:a*b)

def aa(a,b,fun):
	print(fun(a,b))
aa(1,4,lambda a,b:a+b)





























