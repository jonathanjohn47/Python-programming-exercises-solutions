import numpy as np
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
x = []
for i in range(1,m+1):
	a = []
	for j in range(1,n+1):
		a.append(i*j)
	x.append(a)
x = np.array(x)
print(x)
