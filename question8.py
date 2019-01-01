s = str(input("Enter some words: "))
x = s.split(' ')
for i in range(len(x)):
	for j in range(len(x)-1-i):
		if(len(x[j])>len(x[j+1])):
			t = x[j+1]
			x[j+1] = x[j]
			x[j] = t
		else:
			pass
print(x)
