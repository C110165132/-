n=[]
for i in range(5):
    x=input()
    if x=='A':
        x=1
    if x=='J':
        x=11
    if x=='Q':
        x=12
    if x=='K':
        x=13
    n.append(int(x))  
    print(sum(n))