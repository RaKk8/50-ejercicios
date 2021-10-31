precio = int
iva = 19
while True:
    try:
        precio = int(input("Ingrese el precio: "))
        break
    except:
        print("Por favor ingrese unicamente valores numericos")
        continue
if precio>=150000:
    print("El precio normal es",precio," - El valor del iva es {}%".format(iva)," - El precio final con descuento es",((precio*(iva-5))/100)+precio)
else:
    print("El precio normal es", precio, " - El valor del iva es {}%".format(iva), " - El precio final es",((precio * iva) / 100) + precio)