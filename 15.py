x=(input('輸入一組四位數為'))
x2=list(x)
x3=list(map(int,x2))
y=[]
c=(x3[2]+7)%10
y.append(c)
d=(x3[3]+7)%10
y.append(d)
a=(x3[0]+7)%10
y.append(a)
b=(x3[1]+7)%10
y.append(b)
for i in y:
    print(i,end='')