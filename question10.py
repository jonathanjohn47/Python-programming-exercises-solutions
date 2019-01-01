s = str(input("Enter a sentence: "))
x = s.split()
y = []
for i in range(len(x)):
	if x[i] in y:
		pass
	else:
		y.append(x[i])
output = ""
for i in range(len(y)):
	output = output + y[i] + " "
print(output)
