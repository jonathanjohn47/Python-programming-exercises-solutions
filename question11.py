def bintodec(b):
	x = []
	for i in range(len(b)-1, -1, -1):
		x.append(int(b[i]))
	t = 0
	for i in range(len(b)):
		t = t + (x[i]*2**i)
	return (t)

s = str(input("Enter the numbers: "))
x = s.split()
n = len(x)
y = []
for i in range(n):
	y.append(bintodec(x[i]))
z = []
for i in range(n):
	if(y[i]%5==0):
		z.append(x[i])
	else:
		pass
for i in range(len(z)):
	print(z[i], end = ' ')
