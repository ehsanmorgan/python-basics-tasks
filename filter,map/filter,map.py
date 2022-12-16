
names=('ehsan','ahmad','hasn','mahmoud')
title=[x.title() for x in names ]
print(title)





names1=[]
for x in names:
      names1.append(x.upper())
print(names1)


def ehsan(y):
      return y.lower()
names3=filter(ehsan,names)
print(list(names3))



def mytitle(x):
      return x.title()
names4=map(mytitle,names)
print(list(namestitle))




sett={'my','my', 'name', 'name', 'is', 'is', 'is', 'ehsan', 'ehsan', 'ehsan'}
print(sett)
