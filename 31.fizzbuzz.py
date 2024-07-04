"""
writes out numbers 1-100
if number = /3 = write fizz
if number = /5 = write buzz 
if number = /3 and /5, write fizzbuzz 
"""

limit = 100
for i in range(1, limit):
	if i % 3 == 0 and i % 5 == 0:   print('fizzbuzz')  
	elif i % 3 == 0:                print('fizz')
	elif i % 5 == 0:                print('buzz')
	else:                           print(i) 

