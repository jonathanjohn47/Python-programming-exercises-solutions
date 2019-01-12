n = int(input("Enter number of transactions: "))
x = []
for i in range(n):
	x.append(str(input()))

total = 0
z = []
for i in range(len(x)):
	y = x[i].split()
	print(y)
	if (y[0] == 'D'):
		z.append(int(y[1]))
	elif(y[0] == 'W'):
		z.append(-int(y[1]))
	else:
		pass
	y = []
print("Total = ", sum(z))
