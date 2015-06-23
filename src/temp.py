#temp.py functions 
"""
woo
woo
woo
woo
yeah!
lol
"""
def f_to_k(F):
	K = ((F-32.0)*(5.0/9.0)+273.15)
	return K
def k_to_c(F):
	return F - 273.15
def f_to_c(F):
	temp_k = f_to_k(F)
	result = k_to_c(temp_k)
	return result
print(f_to_k(32))
print (f_to_k(212))
print (k_to_c(273.15))
print (f_to_c(32))
#woo
