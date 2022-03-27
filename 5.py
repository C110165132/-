x=int(input('請輸入階乘值m:'))
index=i=1
while index>0:
    index+=1
    i=i*index
    if i>x:
       break
print(f'超過m為{x}的最小階層n值為:{index}')