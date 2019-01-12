s = int(input("Enter a single digit: "))
a = str(s)
n = int(input("Enter the number of repetition: "))

x = []
for i in range(1,n+1):
	x.append(a*i)
z = []
for i in range(len(x)):
	z.append(int(x[i]))
print(z)
y = 0
for i in range(len(x)):
	y = y+int(x[i])

print(y)
