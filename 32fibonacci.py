''' 
based on math monks - 
Fn = Fn-1 + Fn-2, where n > 2

Fn is one variable, we will call it fn 
Fn-1 is another, lets call this fx
and fn-2 is another, lets call this fy 
'''
a = 1
b = 1
for _ in range(10):
	f = a + b
	print(f)
	b = a 
	a = f
