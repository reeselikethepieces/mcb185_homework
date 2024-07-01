"""
oligo melting temp (Tm) 
	1. define function
		def oligo_temp vs. oligo_melt vs. oligo_C vs. oligo_tm vs oligo_Tm
	2. give nt's values 
	3. enter conditions 
		if <= 13 return equation 1
		else return equation 2
	4. plug in and try 
? - do we need to have elif as the second equation and have the else be if sum(oligs) = 0 return none or math.nan 
"""

def oligo_tm(A, T, G, C):
	if (A + T + G + C) <= 13: return (A + T)*2 + (C + G)*4
	else:                     return 64.9 + 41*(G + C - 16.4) / (A + T + G + C)
	
print(oligo_tm(3, 3, 2, 2)) 	#less than 13
print(oligo_tm(44, 44, 27, 27)) #more than 13