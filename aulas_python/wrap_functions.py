
k = 8

def matriz_A(x):

	y = 2*x + k
	
	return y
	
	
def wrapper_matriz_A(k):

	def matriz_A_eff(x):
	
		y = 2*x+k
		
		return y
	
	return matriz_A_eff


print(matriz_A(5))

k = 10

print(matriz_A(5))

