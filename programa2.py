t=int
while t!=5:
    p=int(input("Ingrese el digito 1: "))
    s=int(input("Ingrese el digito 2: "))
    t=int(input("Ingrese la operación a realizar: \n 1.Suma \n 2.Resta \n 3.Multiplicación \n \
4.Division \n 5.Salir \n Digite su opción:  "))
    if t==1:
        suma1=p+s
        print("El resultado de la suma es: ",suma1)
    elif t==2:
        res=p-s
        print("El resultado de la resta es: ",res)
    elif t==3:
        mul=p*s
        print("El resultado de la multiplicación es: ",mul)
    elif t==4:
        if s==0:
            print("ERROR NO ES POSIBLE LA DIVISION POR 0")  
            break
        div=p/s
        print("El resultado de la división es: ",div)
    elif t!=1 and 2 and 3 and 4 and 5:
        print("ERROR: LA OPCION NO SE ENCUENTRA EN EL MENU")    
print("FIN DEL PROCESO")
        
