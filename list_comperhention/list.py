

# list comperhension

numbers =[10,20,30,40,50,60]
a=[x**2 for x in numbers]
print(a)


w=[x**2 for  x in [10,20,30,50] ]
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


x=1
y=1
z=2
n=3
ehsan = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print (ehsan)







names3=['aslan','ehsan','amjad']
new_name2=[]
for x in names3:
      new_name2.append(x.upper())
print(new_name2)
