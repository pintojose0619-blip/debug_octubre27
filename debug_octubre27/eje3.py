def numero_digi(num):
    contador = 1
    while num // 10 != 0:
        contador += 1
        num = num // 10
    return contador
def es_narcisista(num):
    sum = 0
    cont =  numero_digi(num)
    while num > 0:
        digito = num % 10
        sum += digito**cont
        num = num // 10
    return sum
def menu ():
    print("1.validar si es numero narcisista",
          "\n0. salir")
    return
print("Bienvenido al sitema de validacion de numeros narcisistas")

while True:
    menu()
    seleccion = int(input("\ningrese su seleccion "))
    if seleccion == 1:

        num = int(input("\nDigite un número: "))

        print("\nCantidad: ", numero_digi(num))

        if num == es_narcisista(num):
           print("Es narcisista.")
           input("\npresiona ENTER para continuar")
        else:
            print("No es narcisista")
            input("\npresiona ENTER para continuar")
            
    elif seleccion == 0:
        break
    else:
        print("Por favor dijite un valor valido")
        input("\npresiona ENTER para continuar ")
        continue