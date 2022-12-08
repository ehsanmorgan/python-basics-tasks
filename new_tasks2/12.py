'''
x={}
k=[]
p=[]
m=[]
a=[]
b=[]
s = input()
l=list(s)
for i in l:
      if i not in k:
            k.append(i)
for i in k:
      q=l.count(i)
      p.append(q)
for i in range(len(k)):
      x[k[i]]=p[i]

      y=sorted(x)
for i in y:
      a.append(i)
      b.append(x[i])
for i in range(0,3):
      print(a[b.index(max(b))],b[b.index(max(b))])
      b[b.index(max(b))]=0
'''

