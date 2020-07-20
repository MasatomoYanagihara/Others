sum = int(input('鶴と亀の個体数の総和を入力してください。 '))
leg = int(input('足の数の総和を入力してください。 '))
flag = 0

for i in range(100):
    count = 2*i + 4*(sum-i)
    if count == leg:
        flag = 1
        break

if flag == 1:
    print('鶴は', i, '羽、亀は', 100-i, '匹')
else:
    print('式が成立しません。')