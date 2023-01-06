# Python Loops Tasks


#1 Print numbers from 0 to 10 using while

x =1
while x < 11:
      print (x)
      x +=1

#2. Print numbers from 0 to 1o using for

numbers = (0,10)

for x in range(0,12):
       print (x)
       
#3 Stop the loop if the number = 5


for x in range(0,11):
      if x ==5:
            break
      print (x)

#4 Skip the 5 iteration from print

for x in range(0,11):
      if x ==5:
            continue
      print (x)

#5 Print multiplication table from 1 to 5

for x in range (1,6):
      for y in range(1,6):
            print ( f'{x} X {y} = {x*y} ' )


#6 How to get numbers from 10 to 20 using range

for x in range (10,21):
      print (x )


#7 How to get numbers from 10 to 100 with 3 at each
 #step using range

list (range(10,101,3))

[10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100]


#8 Get a list of even numbers from 1 to 100 using for


#9 Get a list of even numbers from 1 to 100 using while

x =1
while x< 101:
      print (x)
      x +=1



#10 Get a list of even numbers from 1 to 100 using range

for x in range(0,101):
      print (x)
















