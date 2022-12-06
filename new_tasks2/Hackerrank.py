
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














 










































