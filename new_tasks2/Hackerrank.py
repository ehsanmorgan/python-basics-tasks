
def is_leap(year):
      
      leap=False
      if year in range(1900, 10**5+1):
            if year%4==0:
                  leap=True
                  if year%400==0:
                        leap=True
                  elif year%100==0:
                        leap=False
      
      
     
    
    # Write your logic here
    
      return leap

year = int(input())
print(is_leap(year))



n = int(input())
for n in range(n+1):
      if n>=1 and n<=150:
            print(n,end='')


'''
if __name__ == '__main__':
    n = int(input())

    if n < 2 or n > 10:
        print("The input number is bigge than 10 or smaler than 2!")
        exit()

    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    
    the_avrage_list =  student_marks[query_name]
    for x in the_avrage_list:
        if x < 0 or x > 100:
            print("The score is bigger than 100 or is smaler than 0!")
            exit()
    if len(the_avrage_list) > 3 or len(the_avrage_list) < 1:
        print("The length of markes array is bigger than 3 or smaler than 1 !")
    
    avrage = format(sum(the_avrage_list)/len(the_avrage_list),'.2f')
    
    print(avrage)
    

    
'''

    









import re

string = input()
S=(re.findall(r'\w',string))

if (len(S)>100):
    exit()

vowels = []
count=0
for x in S :
    if any ([x=="o" , x== 'a' , x=='i' , x=='u' , x=='e' , x=="O" , x== 'A' , x=='I' , x=='U' , x=='E']):
        vowels.append(x)
    else :
        if len(vowels)>=2:
          print( ''.join(vowels))
          count =+ 1
        vowels.clear()
if (count == 0):
    print(-1)
 











 










































