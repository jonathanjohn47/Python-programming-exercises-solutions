z = []
for i in range(1000,3001):
	j = str(i)
	flag = False
	for x in range(4):
		if (int(j[x])%2!=0):
			flag = True
			break
		else:
			flag = False
	if(flag == False):
		z.append(i)

print(z)
