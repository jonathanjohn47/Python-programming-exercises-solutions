s = str(input("Input a string: "))
x = []
for i in range(len(s)):
	if(s[i]== ' '):
		pass
	else:
		x.append(s[i])
letters = []
numbers = []
for i in range(len(x)):
	if(x[i].upper()!= x[i]) or (x[i].lower() != x[i]):
		letters.append(x[i])
	else:
		numbers.append(x[i])

print("Letters = " , len(letters))
print("Numbers = " , len(numbers))
