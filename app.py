numeros_almaceno = []
numeros = input("Ingrese la lista de numeros, cuando finalices puedes colocar la letra s: ")

#genero un ciclo while para recibir la cantidad de numeros en una lista
while numeros != "s":
    numeros_almaceno.append(str(numeros))
    numeros = input("Ingrese la lista de numeros, cuando finalices puedes colocar la letra s: ")
numero_elegido = input("Escriba el numero que se buscara en la lista: ")

finalizar = True
n = 0
m = 1

#genero un ciclo while para realizar las iteraciones entre la lista y realizar los calculos necesarios
#realizo unas decisiones if para validar que los numeros no se repitan
while finalizar:
    if (int(numeros_almaceno[n]) + int(numeros_almaceno[m])) == int(numero_elegido):
        print("Pareja "+str(numeros_almaceno[n])+" y "+str(numeros_almaceno[m]))
        numeros_almaceno.pop(n);numeros_almaceno.pop(m-1);

        n = 0;m = 1;          
    else:
        m = m + 1

    if int(len(numeros_almaceno)) == m:
        m = 0
        n = n + 1
    if int(len(numeros_almaceno)) == n:
        finalizar = False;    

## Desarrollado por johnnathan Castillo Duarte 


input("Presiona Enter para finalizar ")



