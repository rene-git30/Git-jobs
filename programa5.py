palabra="Prueba"
tamaño=len(palabra)
for i in range(tamaño): 
    if i==4:
        continue
    print(palabra[i], "Posición ",i)
print("FIN")
