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
			for i in range(starting value*, up-to value, increments value*)
				* can be removed if your starting value is 0 and increment, increases by 1 
	for item in container
		'for' loops can be used to loop over items in a container
			items in the container are characters | 'strings' are the container
			(Ex 5.0 and 5.1) 
		up to this point, 
nested loops ~ 31fizzbuzz.py
	loops inside other loops 
	conditionals can be inside loops and vice-versa
	in seq alignment, a pair of letters is given a score
			+1 = match		 	-1 = mismatch
	scoring matrix = all possible pairings of letters
		full matrix: inner loop starts at 0
		half matrix + major diagonal: inner loop starts at i 
		half matrix - major diagonal: inner loop starts at i + 1 
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
	most "for i in range()" loops increment by 1 
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
Ex 5.0 'hello' string has 5 characters
Ex 5.1 nt and aa vs.
"""
for char in 'hello':
	print(char)

seq = 'GAATTC'
for nt in seq:
	print(nt)

"""
nested loop ex
print(outerloop, innerloop, value) 
"""
for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')

"""
nested loop ex with abstraction
"""
nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')

"""
scoring matrix
i.e. phylogenetics, distance from spp1 to spp2 (distance is the same in both directions)
	thus, no point in specifiying both distances
	given, 4 spps, we initialize the inner loop one beyond (+1) the current value of the outer loop
"""
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)
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