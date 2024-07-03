"""
### algorithms ###
Iteration 
	while
		- simplest type of loop
			while boolean expression is True>:
				do_something
			(Ex1 below)
		- ^C breaks you out of a running loop
			alternatively, you could use a break statement
				(ex) let 'i' = variable to store an integer 
					each time through the loop, i increases: i + i + 1 
					once i reaches 3, the loop breaks (similar to a sum) 
			(Ex2 below)
		- an even better way to break a 'while' loop is to provide some kind of condition where 
		  boolean expression is no longer true 
			(Ex3 below)
			(Ex 4.0 below) - demonstrates how a loop does not have to start at 0 and has different 
				????? paremeters? 
	for i in range()
		- most loops in python are `for` loops 
			(Ex 4.1 below) 
			for i in range(starting value, up-to value, increments value)
	for item in container
nested loops ~ 31fizzbuzz.py
algorithms
practice problems
practice solutions
	triangular()
	factorial()
	euler()
	is_perfect_square()
	is_prime()
"""


"""
Ex1
while True:
	print('hello')
"""

"""
Ex2
"""
i = 0
while True:
	i = i + 1
	print('hey', i)
	if i ==3: break

"""
Ex3
"""
i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of 1 is', i)

"""
Ex 4.0
shows i starting at 1, ending before 10 and skipping by 3
"""
i = 1 
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)


"""
Ex 4.1
for i in range(starting value, up-to value, increments value): -  reese words
for i in range(initial value, end-before limit, increment*): - korf
			*most "for i in range()" loops increment by 1 
				ergo, can remove increment and have it as, Ex 4.2
Ex 4.2 
for i in range(initial value*, end-before limit)
			*most "for i in range()" loops, initial value/start at 0
				ergo, can remove initial value and have it as, Ex 4.3
Ex 4.3
for in in range(end-before): 

lines 89-91 literally mean the same thing
"""
for i in range(1, 10, 3): print(i)

for i in range(0, 5, 1):  print(i)
for i in range(0, 5):     print(i)
for i in range(5):        print(i)


"""
/ysp
limit = 100
for i in range(1, limit):
	for j in range(i+1, limit):
		d = (i**2 + j**2)**0.5)
		if d % 1 == 0:
		if d // 1 == d:
		
		intd = d // 1 
		print((i,j, d, ind)

	limit = 100
for i in range(1, limit):
	for j in range(i+1, limit):
		d = (i**2 + j**2)**0.5)
		intd = d // 1 
		print((i,j, d, ind)
		
	limit = 100
for i in range(1, limit):
	for j in range(i+1, limit):
		d = (i**2 + j**2)**0.5)
		intd = d // 1 
		r = d % 1
		floor = math.floor(d)
		print(i, j, d, intd, r, floor, math.ceil(d))
		
	A	B	C	D
A		x	x	x
B			x	x
C				x
D
"""