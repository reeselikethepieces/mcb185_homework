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
				 parameters or arguments 
					positional arguments - specifically 
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
	most are a mixture of loops and conditionals, and are often contained inside fxns 
	in ex, create algorithm  with the goal to calculate the GC compo of a nt seq 
		the fxn needs an input seq, called 'seq' 
		then, the fxn needs to examine each nt and keep track of how many Gs and Cs it finds
			keeping track via stored in variable 'gc_count'
		also need total number of nts, which we'll store in a variable called total 
	(Ex 6.0 below)
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
symmetrical along the diagonal 
"""

"""
Ex 6
"""
def gc_comp(seq):
	gc_count = 0 
	total = 0 
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total
	
print(gc_comp('ACAGCGAAT'))

"""
most algorithms follow the 3-part structure:
	1. initialization (lines 187-)
	2. iteration (lines 197-200)
	3. Finalization (196) 

	1. gc_comp() has two initializations
		setting gc_count = 0
		setting total = 0 
	2. loop over nt of the seq (nt(seq)) 
		notice block structure. only when nt's c and g, should gc_count get incremented
		however, all nts must be counted 
			tis y gc_count is indented inside the 'if' block but the 'total' is not
	3. final step is dividing gc_count by total 
"""

"""
Practice Problems
"""

"""
1. write fxn
	def fxname(variable):
2. sum of #'s from 1 to n 
	i = 1, l = n 
	for i in range(initial, end-range, increment) 
				  (0, n, 1) can be simplified to (n)
3. we know that 21 is the triangular number of 6, so double check the program runs
"""

def triangular(n):
	tri = 0 
	for i in range(n+1):
		tri = tri + i
	return tri
print(triangular(6))


"""
factorial
"""


def factorial(n):
	if n == 0: return 1
	fac = 1 
	for i in range(1, n+1): 
		fac = fac* i
	return fac
	
print(factorial(4))

"""
Euler's numbere(2.71828) 
infinite sum of 1/n! 
"""
'''how to print this one to check that it works?
$import math
print(euler(math.e))$
'''
def euler(limit):
	e = 0 
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e

"""
if n == perfect square 
i.e. 4, 9, 16, 25 are perfect squares bc square roots are integers
	this means we do not want a remainder or a neg number	
"""
import math

def is_perf_sqr(n):
	root = math.sqrt(n)
	if root % 1 == 0: return True
	return False
	
print(is_perf_sqr(81))
print(is_perf_sqr(56))
print(is_perf_sqr(100))
'''
how to make this one work?
is it even worth it? the idea to call two other existing functions in a new fxn?
prints None

import math

def is_integer(n):
	if n % 1 == 0: return True
	return False

def is_not_complex(n):
	if n >= 0 and n <= 1: return True
	return False

def is_perf_sqr(n):
	if n == is_integer and is_not_complex:
		return math.sqrt(n) 
	
print(is_perf_sqr(81))
print(is_perf_sqr(56))
print(is_perf_sqr(100))
'''

"""
prime
google - a whole number greater than 1 that cannot be 
exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
"""

'''
why doesnt this work

def is_prime(n):
	x != n
	n >= 1
	if n // n or n // 1: return True
	elif n // x: return False
	return False 
'''

def is_prime(n):
	for den in range(2, n+1):
		if n % den == 0: return False
	return True 

print(is_prime(5))	#is prime but returns False
print(is_prime(19)) # ""
print(is_prime(22))	
print(is_prime(3))	# ""
print(is_prime(6))	
print(is_prime(3))	# ""


"""
This algorithm features a short-circuit (line 3). It returns False as soon as it finds any 
factor smaller than itself. If it fails to find any factors, it eventually returns True.
"""