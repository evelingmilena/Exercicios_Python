import numpy as np

N = 10
h = np.pi/N
w = 1.7
N_it = 10000
matrizU = np.zeros((N+1,N+1),float)
matrizU_exata = np.zeros((N+1,N+1),float)
matrizU_erro = np.zeros((N+1,N+1),float)

#Atribuindo condicao de contorno x = pi. As outras automaticamente são nulas. Portanto, não precisa ser atualizado, pois a matriz foi declarada nula no início.
for j in range(N+1):
	matrizU[N][j] = np.sinh(np.pi)*np.sin(j*h)

#print(matrizU)

#Método de Gauss-Seidel
for k in range(N_it):
	for i in range(1,N):
    		for j in range(1,N):
        		matrizU[i][j] = 0.25 * w * ( matrizU[i+1][j] + matrizU[i-1][j] + matrizU[i][j+1] + matrizU[i][j-1] ) + ( 1. - w ) * matrizU[i][j]

#print(matrizU)    

erro_quad = 0.0
for i in range(N+1):
	for j in range(N+1):
		matrizU_exata[i][j] = np.sinh(i*h)*np.sin(j*h)
		matrizU_erro[i][j] = matrizU_exata[i][j] - matrizU[i][j]
		erro_quad += matrizU_erro[i][j]**2
		
print(matrizU)
print("Erro quadrático é:", erro_quad)


