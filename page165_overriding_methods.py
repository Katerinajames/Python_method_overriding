
class A:
 def print(self):
	 print('Hello I am a')
	
	
	
class B(A):
	def print(self):
	 print('Hello I am b')
 
 
print("-----------------------")
print('Objects')
a=A()
a.print()
b=B()
b.print()
print("-------------------------------")
print('Table')
t=[a,b]

for i in t:
	i.print()



