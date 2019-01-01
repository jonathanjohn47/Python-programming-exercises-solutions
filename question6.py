#Q = Square root of [(2 * C * D)/H]
import numpy as np
D = []
C = 50
H = 30
n = int(input("How many numbers: "))
for i in range(n):
	D.append(int(input()))
print(D)

E = []
for i in range(n):
	E.append(np.sqrt(2*C*D[i]/H))
print(E)
