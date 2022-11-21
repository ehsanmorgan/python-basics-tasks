


print(list(x for x in range(0,101,2) )  )


x =0
while x< 101:
      print (x)
      x +=2


even=[x for x in range(0,101) if x%2 ==0 ]
print (even)



def numbers (x,y):
      even=[]
      for x in range (x,y+1):
            if x%2 ==0:
                  even.append(x)

            

      print(even)

numbers(1,101)




def no_duplicate (x):
      words=x.split(' ')
      new_words=[]
      for w in words:
            if w in new_words:
                  continue

            else:
                  new_words.append(w)
      print(' '.join(new_words))    
no_duplicate('my my my my my name name name name is is is is is ehsan ehsan ehsan ehsan')

      

















