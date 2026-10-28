def abundantes(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    return sum > num

def menu ():
    print("1.Realizar consulta",
          "\n0. salir")
    return
print("Bienvenido al sitema de numeros abundantes")
while True:
    menu()
    seleccion = int(input("\ningrese su seleccion "))
    if seleccion == 1:
        inicial = int(input("\nDigite un numero incial: "))
        final = int(input("\nDigite un numero final: "))

        for i in range(inicial, final + 1):
            if abundantes(i):
                print(i)
                
            else:
                pass
        input("\npresiona ENTER para continuar")
    elif seleccion == 0 :
        print("gracias por usar nuestro sistema")
        break 
    else:
        print("Por favor dijite un valor valido")
        input("\npresiona ENTER para continuar ")
        continue