
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
	d = (b**2 - 4 * a * c)
	if d == -d: return math.nan 
	x1 = -b + math.sqrt(d)/(2*a)
	x2 = -b - math.sqrt(d)/(2*a)
	return x1, x2 
	
print(quadratic(2, 12, 3))

