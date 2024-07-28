'''
program - not fxn 
pythagorean triples for triangles with sides a and b < 100
i.e. 3, 4, 5 is a triple - 3**2 + 4**2 = 5**2
all sides must be integer (hint) - believe this means use, i, but also means no floating #s
	oof, his next line says a good way to test for an integer is...
		if c % 1 == 0 (this is what was used previously for perfect square
62 unique triples (in the half matrix minus the major diagonal of comparison) 
'''

limit = 100
for a in range(1, limit):
	for b in range(a+1, limit):
		c = (a**2 + b**2)**0.5
		if c % 1 == 0: print(a, b, c, sep='  ')
			