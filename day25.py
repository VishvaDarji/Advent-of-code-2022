#referred to AOC reddit pages

 with open('day25.txt', mode="rt") as f:
        day25_data = f.read().splitlines()


snafu_to_decimal=[]
for snafu_num in day25_data:
    sub=[]
    for i, n in zip(range(len(day25_data)),snafu_num.strip()[::-1]):
        if n=='=':
            sub.append((5 ** i) * -2)
        elif n=='-':
            sub.append((5 ** i) * -1)
        elif n=='0':
            sub.append((5 ** i) * -0)
        elif n=='1':
            sub.append((5 ** i) * 1)
        elif n=='2':
            sub.append((5 ** i) * 2)
        
    snafu_to_decimal.append(sum(sub))

decimal_num=sum(snafu_to_decimal)

carry=0
snafu=[]
while decimal_num>0:
    x = decimal_num % 5 + carry
    if x==2:
        snafu.append('2')
    elif x==1:
        snafu.append('1')
    elif x==0:
        snafu.append('0')
    elif x==3:
        snafu.append('=')
    elif x==4:
        snafu.append('-')
    elif x==5:
        snafu.append('0')

    if x > 2:
        carry=1
    else:
        carry=0
    
    decimal_num //= 5

print(''.join(snafu[::-1]))
