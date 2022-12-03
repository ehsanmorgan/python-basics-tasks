

# list comperhension

numbers =[10,20,30,40,50,60]
a=[x**2 for x in numbers]
print(a)


w=[x**2 for  x in [10,20,30,40] ]
print(w)





s=[x for x in range(1,101) if x %2 ==0]
print(s)


names=('amjad' , 'ahmad' , 'hasn')
d=[x.title() for x in names]
print(d)


f=[x.upper() for x in ['ehsan aslan ali']]
print(f)

m=[len (x) for x in  [ 'ehsan' , 'ali' , 'aslan']]
print(m)




num=[True if x%2 ==0  else False for x in range(1,101) ]
print(num)
