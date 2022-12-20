#1 Creat a simple funcation that takes 2 numbers and print the vaieus

def mysum (w,s):
      print(w+s)

mysum(13,43)


#2 Creat a simple funcation that takes 2 numbers and return the vaieus

def mysum(x,y):
      return (x+y)

f=mysum(12,9)
print(f)


#3 in the above return function ,use keyword argumnts when caling the function


def mysum(x,y):
      return (x+y)

f=mysum(x=9, y=13)
print(f)




#4 in the above return function ,give x and y default values of 0 and call thr function

def mysum(x=0,y=0):
      return (x+y)

f=mysum()
print(f)


#5 Creat a function that can take any numbers  of the arguments and print the sum of them

def ehsan(arg,*vartuple):
      result=arg+sum(vartuple)
      return result
     
      

d=ehsan(5,6,8,9,10,20)
print(d)


#6 Creat the same sum function using the lambda

ehsan = lambda x,y : x+y

e= ehsan (21,32)
print (e)



k=ehsan (123213,4234)
print (k)



#7 call the lambda function at ehr same definition ine 

mysumm=(lambda l,o : l+o) (43,23)
print(mysumm)



#8 writte the diference between the local variable and global variable







































