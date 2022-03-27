x=eval(input('請輸入西元年:'))
x=(x-1900)%12
if x==0:
    print('鼠')
elif x==1:
    print('牛')
elif x==2:
    print('虎')
elif x==3:
    print('兔')
elif x==4:
    print('龍')
elif x==5:
    print('蛇')
elif x==6:
    print('馬')
elif x==7:
    print('羊')
elif x==8:
    print('猴')
elif x==9:
    print('雞')
elif x==10:
    print('狗')
else:
    print('豬')