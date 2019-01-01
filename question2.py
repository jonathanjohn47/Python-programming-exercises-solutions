x = int(input("Enter a number: "))
def factorial(n):
	if (n==1):
		return 1
	else:
		y = n*factorial(n-1)
		return y

print(factorial(x))
