# 20demo.py by reese   

import math      

print('hello, again') # greeting

print(1.5e-2)

print(1 + 1)
print(1 - 1)
print(2 * 2)
print(1 / 2)
print (2 ** 3)
print(5 // 2)
print(5 % 2)
print(5 * (2 + 1))

print(math.log(2))
print(math.sqrt(2))
print(math.pow(2, 3))

print(0.1 *1)
print(0.1 * 3)

a = 3                       # side
b = 4                       # side  
c = math.sqrt(a**2 + b**2)  # hypotenuse 
print(c)

print(type(a), type(b), type(c))
print(type (a), type (b), type(c), sep=', ')

"""
print(1 / 0)            # divide by zero error
print(math.log(0))      # math domain error
print(math.sqrt(-1))    # math domain error
print((-1)**0.5)        # complex number, not a math domain error 


print(math.ceil(x)) 
print(math.floor(x))
print(math.log2(x))
print(math.log10(x))
print(math.factorial(n))
"""
 
"""practice problems 
1. Write a function that turns negative numbers into positive numbers and vice versa. 
Give your function a name that is simultaneously simple and descriptive.
    (-) --> (+) 
    (+) --> (-)
        --> to make a neg#, should we x by -1
            --> name: inverse
"""
def inverse(a): 
	return -1 * a

print(inverse(1))


"""practice problems
2. Write functions that compute the areas, circumferences, or volumes of simple shapes 
like squares, rectangles, circles, spheres, etc.  - area_circle
	a = math.pi*(r**2)      
"""
def area_circle(r):
	return math.pi * r**2

print(area_circle (8))


"""practice problems 
3.  Write functions that convert temperature (whichever scales you prefer).
	F --> K 
		C = K - 273.15
		C = (F - 32) * 5/9
		C = C 
			K - 273.15 = (F - 32) * 5/9
				+ 273.15 = + 273.15
				-------------------
			K = (F - 32) * 5/9 + 273.15 
"""
def temp_ftok(f):
	return (f - 32) * 5/9 + 273.15

print (temp_ftok(69))


"""practice problems 
4. Write functions that convert speeds (mph, kph, fps, mps, etc).
    mph --> kph 
"""
def mph_to_kph(m): 
	return (m*1.60934)

print (mph_to_kph(60))


"""practice problems 
5. Write a function that computes DNA concentration from OD260.
    # this was before looking up OD260, and seeing "people also asked" how to calc [DNA] from OD260
    OD260 --> DNA 
        let DNA = d and OD260 = o and df = dilution factor 
	[dsDNA] = 50 ug/mL * OD260 * dilution factor(df)
		let d = [dsDNA] and OD260 = o and dilution factor = df 
		one OD260 = 33 ug of DNA 
"""
def od260(df):
	return (50 * 30 * df)

print (od260(4))


"""practice problems 
6. Write a function that computes the distance between two points in a graph.
	given two coordinate points (x1, y1) and (x2, y2)
		d = sqrt.(x2 - x1)**2 + (y2 - y1)**2)
"""
def distance_twopoints (x1, y1, x2, y2):
	
	return (math.sqrt((x2 - x1)**2 + (y2-y1**2)))

print(distance_twopoints(2,3,6,10))


"""practice problems
7. Write a function that computes the midpoint between two points. Note that this function 
must return values for x and y. Your return statement will have two values separated by a comma. 
	Your function will look something like this.
		def midpoint(x1, y1, x2, y2):
Call your function like this: x, y = midpoint(x1, y1, x2, y2).
	Midpoint formula: ((x1 + x2)/2, (y1+y2)/2) 
"""
def midpoint(x1, y1, x2, y2):
	return (x1+x2)/2, (y1+y2)/2

print(midpoint(2, 3, 4, 10))

