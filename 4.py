n=int(input('請輸入x座標:'))
n2=int(input('請輸入y座標:'))
if n<0 and n2>0:
    print('該點位於第一象限')
elif n>0 and n>0:
    print('該點位於第二象限')
elif n<0 and n2<0:
    print('該點位於第三象限')
elif n==0 and n2==0:
    print('該點位於原點')
elif n==0 and n2<0 or n2>0:
    print('該點位於y軸上')
elif n<0 or n>0 and n2==0:
    print('該點位於x軸上')
else:
    print('該點位於第四象限')
n3=((n-0)**2+(n2-0)**2)**0.5
print(f'離原點距離為:{n3}')