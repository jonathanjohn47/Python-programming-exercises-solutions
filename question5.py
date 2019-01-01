class string:
	def __init__(self):
		self.s = ""
	def getstring(self):
		self.s = str(input("Input a string: "))
	def printstring(self):
		print(self.s)

st = string()
st.getstring()
st.printstring()
