import math

x=int(input('輸入月租費形式:'))
x2=int(input('輸入通話時間:'))
if x==186:
    x2=x2*0.09
    if x2<186:
        print(f'通話費為186')
    elif 186<=x2<372:
        x2=x2*0.9
        print(f'通話費為{round(x2)}')
    else:
        x2=x2*0.8
        print(f'通話費為{round(x2)}')
elif x==386:
    x2=x2*0.08
    if x2<386:
        print(f'通話費為386')
    elif 386<=x2<772:
        x2=x2*0.8
        print(f'通話費為{round(x2)}')
    else:
        x2=x2*0.7
        print(f'通話費為{round(x2)}')
elif x==586:
    x2=x2*0.07
    if x2<386:
        print(f'通話費為586')
    elif 586<=x2<1172:
        x2=x2*0.7
        print(f'通話費為{round(x2)}')
    else:
        x2=x2*0.6
        print(f'通話費為{round(x2)}')
else:
    x2=x2*0.06
    if x2<386:
        print(f'通話費為986')
    elif 986<=x2<1972:
        x2=x2*0.6
        print(f'通話費為{round(x2)}')
    else:
        x2=x2*0.5
        print(f'通話費為{round(x2)}')