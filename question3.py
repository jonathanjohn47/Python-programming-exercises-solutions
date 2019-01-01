dict = {}
n = int(input("How many elements? "))
for i in range(1, n+1):
	k = i
	v = i*i
	dict.update({k:v})
print(dict)
