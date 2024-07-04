""" 
write fxn that returns Shannon entropy (se) for nt counts a,c,t,g 
	from the internet se = sum probabilities*log2(1/pi) 
		l
		E    Pi * log2(1/Pi) 
	  i = 1
	  
			p(x) * log p(x)
	  
name fxn(counts nts):
	
"""

def s_entropy(a, c, g, t):
	total = a + c + g + t 
	pa = a/total
	pc = c/total
	pg = g/total
	pt = t/total
	return pa + pc + pg + pt
print(s_entropy(0, 56, 56, 33))

 