s = str(input("Enter entries separated by space: "))
x = s.split()
y = []
for i in range(len(x)):
	if(int(x[i])%2==0):
		pass
	else:
		y.append(int(x[i])**2)
print(y)
