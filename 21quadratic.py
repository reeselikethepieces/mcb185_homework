
"""
ax**2 + bx + c == 0 
x1 = (-b + math.sqrt(b**2 - 4 * a * c))/2 * a
	x2 = (-b - math.sqrt(b**2 - 4 * a * c))/2 * a

step 1: calculate discriminant
step 2: if d is negative return nan, nan
step 3: calculate x1
step 4: calculate x2
step 5: return x1, x2
"""

import math

def quadratic(a, b, c):
	d = b**2 - 4 * a * c 
	if d < 0: return math.nan, math.nan
	x1 = -b + math.sqrt(d)/(2 * a)
	x2 = -b - math.sqrt(d)/(2 * a)
	return x1, x2

print(quadratic(2, 4, 1))
	


"""
first ran to test if my condition for d worked. How? make a negative d - use values that you can test and know 
will result in -d. 
i.e. for x1 and x2, just put some values to test d. 
	- i.e. x1 = 3
		   x2 = 4 
will inputt, print(quadratic(3, 2, 1)) 
will output, (nan, nan) _if) done correctly.

Once I'm sure that works, then I can add the equations into x1 and x2"""