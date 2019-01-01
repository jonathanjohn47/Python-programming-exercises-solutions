x = list(range(2000,3201))
y = []
for i in range(len(x)):
	if((x[i]%7==0)and(x[i]%5!=0)):
		y.append(x[i])
	else:
		pass
print(y)
