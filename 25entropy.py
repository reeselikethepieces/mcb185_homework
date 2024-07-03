""" 
write fxn that returns Shannon entropy (se) for nt counts a,c,t,g 
	from the internet se = sum probabilities*log2(1/pi) 
		l
		E    Pi * log2(1/Pi) 
	  i = 1
	  
where l = total number = 4 
pi = probability of situation i in the system  = 1/4 = 0.25 
...thought - bc all four probabilities are the same, cant you calculate se for one nucleotide and then multiply by 4
to get the total se for nts
	given different probabilities:
	p1 = 'A'
	p2 = 'C'
	p3 = 'G'
	p4 = 'T'
	if se = p1 * log2(1 / p1): 
"""

def s_entropy(A, C, G, T):
	se1 = 'A' * log2(1 / 'A')
	se2 = 'C' * log2(1 / 'C')
	se3 = 'G' * log2(1 / 'G')
	se4 = 'T' * log2(1 / 'T')
	se = se1 + se2 + se3 + se4
	return se
	'^ACGT':	return 0
print(0.25, 0.25, 0.25, 0.25)