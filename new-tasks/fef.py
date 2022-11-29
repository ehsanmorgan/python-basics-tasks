'''
class calc :
      def mal (self,x,y):
            print (x*y)

      def divid (self,x,y):
            print(x/y)

      def plas(self,x,y):
            print(x+y)
      def __init__(self,name):
            print(f'{name}')

c=calc ('ehsannnnn')
c.mal(10,10)
c.divid(1000,2332)
c.plas(3212,12321)
'''
'''
class student :

      def __init__(self,name):
            print(f'welcome {name}')
            self.marks=[]

      def add_mark(self,mark):
            self.marks.append(mark)

      def get_avg(self):
            avg=sum(self.marks) / len (self.marks)
            print(avg)

amjad=student('amjad')
aslan=student('aslan')
ehsan=student('ehsan')
ali=student('ali')
amjad.add_mark(23)
aslan.add_mark(90)
ehsan.add_mark(80)
ali.add_mark(70)
aslan.add_mark(67)
ehsan.add_mark(65)
aslan.add_mark(90)
amjad.add_mark(50)
ali.add_mark(30)
aslan.add_mark(90)
ehsan.get_avg()
ali.get_avg()
amjad.get_avg()
aslan.get_avg()
print(ehsan.marks)
print(aslan.marks)
print(ali.marks)
print(amjad.marks)


'''







'''

numbers=[x for x in range (1,101) if x%2 ==0 ]
print(numbers)

'''

class users:
      def __init__ (self, name ,age ,adresse):
            self.name=name
            self.age=age
            self.adresse=adresse
            
            print(f'welcome {name}')
            
            
               

      def show_info(self):
            print(f"name    : {self.name}")
            print(f'age       : {self.age}')
            print(f'adresse: {self.adresse}')





class Bank(users):

      def __init__(self,name,age,adresse):
            super().__init__(name,age,adresse)
            self.balance=0
            

      def deposite (self,amount):
            self.balance +=amount
            print(f'deposite succses = {amount} your curent balance = {self.balance}')

            


      def withdrow (self,amount):
            if amount > self.balance :
                  print('your curent balance is not enouth')

                  return


            self.balance -=amount
            print(f'withdrow succse ={amount}   your curent balance = {self.balance}')



            
      def check_balance(self):
            self.show_info()
            print(f'your curent balance = {self.balance}')

b=Bank('ehsan',27,'germany')
b.show_info()

b.deposite(534)
b.deposite(657)
b.deposite(1000)

b.withdrow(213)
b.withdrow(123)
b.withdrow(2000)






b.check_balance()




class test :

      total=0

      def user (self,name):
            print(f'welckome {name}')



c=test()
c.user('ehsan')
print (c.total)





































