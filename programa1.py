n=int
suma=0
mayor=0
menor=int
while n!=0:
    n=int(input("Ingrese el numero:  "))
    suma=suma+n
    if n>mayor:
        mayor=n
    if n!=0:
        if n<mayor:
            menor=n
print("Mayor: ",mayor)
print("Menor: ",menor)
print("Suma:",suma)
print("Termino el programa")