print("Добрый день!Введите число n от 1 до 25")
n=int(input())
if 1<=n<=25:
    d=0
    for c in range(2,n):
        if n%c==0 :
            d=d+1
    if n>=2 and c==0 :
        print("Y")
    else :
        print("N")
else :        
    print("Ошибка")