
names=('ehsan','ahmad','hasn','mahmoud')
n=[x.title() for x in names ]
print(n)





names1=[]
for x in names:
      names1.append(x.upper())
print(names1)


def ehsan(y):
      return y.lower()
names4=filter(ehsan,names)
print(list(names4))



def mytitle(x):
      return x.title()
names3=map(mytitle,names)
print(list(names3))




sett={'my','my', 'name', 'name', 'is', 'is', 'is', 'ehsan', 'ehsan', 'ehsan'}
print(sett)
