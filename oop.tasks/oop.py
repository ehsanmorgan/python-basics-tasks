#1 Explain in few words what we mean by a class and give example

'''
class mean s that we great our own class and we give him a name and a function

'''

# Example

class names :

      def name1 (self,name):
            print (f'hello {name}')

c=names()
c.name1('ehsan')


#2create a simple class names calculator
#3Create a constructor that prints Welcome message
#4 Add 2 methods to the class sum & mull
#5 The sum method return the sum of 2 arguments x ,y
#6 The mull method return the multiplication of the arguments x and y
#7 Take an object from the class
#8 Call the sum method with 10 , 20
#9 Call the mull method with 10 , 20
class calc :

      def __init__(self,name):
            print(f'welcome {name}')
      def sum(self ,x,y):
            print(x+y)

      def mull(self,x,y):
            print(x*y)

cl=calc('ehsan')
cl.sum(10,30)
cl.mull(10,20)











            
