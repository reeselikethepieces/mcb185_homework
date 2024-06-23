# 20demo.py by reese
print('hello again') # greeting

"""
i deleted 20demo.py from git bc the commit name was wrong; 
while brain fried, and thus not thinking,
i deleted the FILE 
it was stupid mistake.
	originally named 20demov2 (as in version 2) but took off for reasons
"""

print(1.5e2)
print(1 +1)
print(1-1)
print(2 *2)
print(1 / 2)
print(2 ** 3)
print(5 // 2)
print(5 % 2)
print(5 * (2+1))

"""
print(XoperatorY)
"""

print(abs(-5))
print(pow(2, 10))
print(round(1.5e2, ndigits=1))
print(round(1593038, ndigits=1))
print(round(15.93038, ndigits=1))
print(round(15.93038, ndigits=4))

'''
did not work
print(math.ceil(9.9)))
print(math.floor(9.9))
why? because the above are the few that don't require the 'import math' statement
'''

"""
math functions
"""
import math 

print(math.ceil(9.5))
print(math.floor(9.5))
print(math.log(2))
print(math.log2(2))
print(math.log10(2))
print(math.sqrt(64))
print(math.pow(2,10))
print(math.factorial(666))
print(math.e)
print(math.pi)
print(math.inf)
print(math.nan)

"""
no_nos
	print(1/0)				# divide by zero error
	print(math.log(0))		# math domain error
	print(math.sqrt(-1))	# math domain error 
	print((-1)**0.5)		# complex number, not a math domain error
"""

"""
variables
"""
a = 3						# side of triangle
b = 4						# side of triangle 
c = math.sqrt(a**2 + b **2) # hypotenuse 
print(c)

"""
type
"""
print(type(a), type(b), type(c))	# sep by a single space
print(type (a), type(b), type(c), sep=',')	# sep by a comma using option sep=''

"""
functions														# represented by keyword 'def'
	def name_of_function										# your unique name for the fxn you create
	def name_of_function(variable1, variable 2, etc.):			# parenthases and colon are added 
	def name_of_function(variable1, variable 2, etc.):	
		return(formula*)										# lines in function = indented; 
																# *formula includes variable(s)
		
	print(name_of_function(variable1, variable 2, etc.)			# call out function w/ print 
"""

"""
1. Write a function that turns negative numbers into positive numbers and vice versa. Give your function 
a name that is simultaneously simple and descriptive.
"""
def inverse(x):
	return(x)
	
print(inverse(1))
print(inverse(-1))

"""
2. Write functions that compute the areas, circumferences, or volumes of simple shapes like squares, 
rectangles, circles, spheres, etc.
	area of circle --> area_circle(variable):
		math.pi r**2 --> formula 
"""
def area_circle(r):
	return math.pi * r**2

print(area_circle(4))

"""
3. Write functions that convert temperature (whichever scales you prefer).
	measuring a Temperature 'temp'											# notice lowercase in nomenclature
		Units are Farenheit to Kelvin --> temp_ftok(f):						# must define (variable) to call out l8r					
		solve for k to get the formula of the desired outcome variable
			k = (f - 32) * 5/9 + 273.15 --> formula 
"""
def temp_ftok(f):
	return (f - 32) * 5/9 + 273.15
	
print(temp_ftok(69))

"""
4. Write functions that convert speeds (mph, kph, fps, mps, etc).
	measuring: speed 
		units mph to kph --> speed_mtok
"""
def speed_mtok(m):
	return m*1.60924

print(speed_mtok(69))

"""
5. Write a function that computes DNA concentration from OD260.
	[dsDNA] = 50 ug/mL * od260 * df
	od260 = 33 ug/[ssDNA] 
		od260 = 66 ug/[dsDNA]
	(50 ug/mL * o *66 ug/[dsDNA] * dfmL)
"""
def od260(o, df):
	return (50 * o * 66 * df)

print(od260(400, 5))

"""
6. Write a function that computes the distance between two points in a graph.
	d = sqrt((x2-x1)**2 + (y2-y1)**2)
"""
def d_of_2pts(x1, x2, y1, y2):
	return (math.sqrt((x2-x1)**2 + (y2-y1)**2))

print(d_of_2pts(3, 4, 6, 10))

"""
7. 	Write a function that computes the midpoint between two points. Note that 
this function must return values for x and y. Your return statement will have two values 
separated by a comma. Your function will look something like this.
	midpoint formula --> (x1+x2)/2, (y2-y1)/2
"""
def midpt_of_2pts(x1, x2, y1, y2):
	return (x1+x2)/2, (y2-y1)/2

print(midpt_of_2pts(3, 4, 6, 10))