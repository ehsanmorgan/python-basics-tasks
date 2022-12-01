#1Create a new class names SciCalc with 3 methods ,
#sum , mull , power all of them takes 2 argument x, y
#2. Sum return the sum of x and y
#3. Mull return the multiplication of x and y
#4. The power return x power y
#5. Take an object from the class and call the 3 methods
#with any numbers








class calc :

      def __init__(self,name):
            print(f'welcome {name}')
      def sum(self ,x,y):
            return(x+y)

      def mull(self,x,y):
            return(x*y)

cl=calc('ehsan')
print (cl.sum(10,20))
print (cl.mull(10,20))


#Inherit from the Calc class , now remove the
#unneeded code the the SciCalc after inheriting
#8. call the 3 methods again from the SciCalc object
#9. Now you should see the same result as before
#10. Explain in few words what happened after inheriting
#Python OOP Tasks Part 2


class scicalc (calc) :
      
            

      def power(self,x,y):
            return(x-y)
      
s=scicalc(calc)
print (s.sum(254,232))
print(s.mull(65,45))
print (s.power(432,654))



























