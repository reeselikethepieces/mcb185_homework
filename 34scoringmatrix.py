''' program (not fxn) 
displayus +1/-1 scoring matrix seen as 
   A  C  G  T
A +1 -1 -1 -1
C -1 +1 -1 -1
G -1 -1 +1 -1
T -1 -1 -1 +1
'''

"""
alphabet = 'ACGT'
match = '+1'
mismatch = '-1'
"""

alphabet = 'ACGT'
match = '+1'
mismatch = '-1'
print('   ', end='')

for nt in alphabet:
	print(nt, end='   ')
print( )

for nt1 in alphabet:
	print(nt1, end=' ')
	for nt2 in alphabet:
		if nt1 == nt2: print(match, end='  ') 
		else: print(mismatch, end='  ') 
	print( )