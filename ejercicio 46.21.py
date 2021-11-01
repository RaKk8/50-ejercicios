num = []
while True:
    try:
        n = int(input("n: "))
        m = int(input("m: "))
        if n>m:
            for x in range(m+1,n):
                num.append(x)
        if m>n:
            for x in range(n+1,m):
                num.append(x)
        break
    except ValueError:
        print("Por favor ingrese unicamente valores numericos")
        continue
print(num)
