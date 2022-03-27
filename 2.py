x=int(input('請輸入用電量:'))
if x<=120:
    a=x*2.1
    b=x*2.1
    print(f'summer months:{a}')
    print(f'summer months:{b}')
elif 120<x<=330:
    a2=120*2.1+(x-120)*3.02
    b2=120*2.1+(x-120)*2.68
    print(f'summer months:{a2}')
    print(f'Non-summer months:{b2}')
elif 330<x<=500:
    a3=120*2.1+(330-120)*3.02+(x-330)*4.39
    b3=120*2.1+(330-120)*2.68+(x-330)*3.61
    print(f'summer months:{a3}')
    print(f'Non-summer months:{b3}')
elif 500<x<=700:
    a4=120*2.1+(330-120)*3.02+(500-330)*4.39+(x-500)*4.97
    b4=120*2.1+(330-120)*2.68+(500-330)*3.61+(x-500)*4.01
    print(f'summer months:{a4}')
    print(f'Non-summer months:{b4}')
else:
    a5=120*2.1+(330-120)*3.02+(500-330)*4.39+(500-700)*4.97+(x-700)*5.63
    b5=120*2.1+(330-120)*2.68+(500-330)*3.61+(500-700)*4.01+(x-700)*4.5
    print(f'summer months:{a5}')
    print(f'Non-summer months:{b5}')