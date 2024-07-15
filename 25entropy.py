""" 
write fxn that returns Shannon entropy (se) for nt counts a,c,t,g 
	from the internet se = sum probabilities*log2(1/pi) 
		l
		E    Pi * log2( Pi) 
	  i = 1
	  
			p(x) * log2 p(x)
	  
name fxn(counts nts):
	
"""
import math


def s_entropy(a, c, g, t):
	total = a + c + g + t
	pa = a/total
	pc = c/total
	pg = g/total
	pt = t/total
	h = 0 
	if pa != 0: h = h - pa * math.log2(pa)
	if pc != 0: h = h - pc * math.log2(pc)
	if pg != 0: h = h - pg * math.log2(pg)
	if pt != 0: h = h - pt * math.log2(pt)
	return h
	
print(s_entropy(0, 56, 56, 33))


def sum3(x, y, z):
	s = 0 
	s = s + x
	s = s + y
	s = s + z
	return s 
print(sum3(3,5,6))

def max3(x, y, z):
	if x >= y and x >= z: return x
	if y >= z: return y
	return z
	 
	
print(max3(7, 5, 9))
print(max3(5, 5, 5))
print(max3(5, 9, 7)) 
print(max3(5, 5, 9))

'''
if   a == 0: return pc*math.log2(pc) + pg*math.log2(pg) + pt*math.log2(pt)
	elif c == 0: return pa*math.log2(pa) + pg*math.log2(pg) + pt*math.log2(pt)
	elif g == 0: return pa*math.log2(pa) + pc*math.log2(pc) + pt*math.log2(pt)
	elif t == 0: return pa*math.log2(pa) + pc*math.log2(pc) + pg*math.log2(pg)
this could take forever. bc what about the situations where there are 2 >= probs that = 0?
want to have it that if print(s_entropy(has any 0 probabilities)) then, skip or count as 0,
then, go to the next and calculate

for pa or pc or pg or pt:
'''