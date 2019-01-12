s = str(input("Input a string: "))
x = []
for i in range(len(s)):
	if(s[i]== ' '):
		pass
	else:
		x.append(s[i])

upper = []
lower = []
for i in range(len(x)):
	if(x[i].upper()==x[i]):
		upper.append(x[i])
	else:
		lower.append(x[i])

print("Upper Case letters = " , len(upper))
print("Lower Case letters = " , len(lower))
