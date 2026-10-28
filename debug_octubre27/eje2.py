
def menu ():
    print("1.validar si es numero perfecto",
          "\n0. salir")
    return
print("Bienvenido al sitema de validacion de numeros perfectos")

while True:
    menu()
    seleccion = int(input("ingrese su seleccion "))
    if seleccion == 1:
        num = int(input("Introduzca su numero: "))
        sum = 0
        if num < 0:
            break
        for i in range(1, num):
            if num % i == 0:
                sum += i
            else:
                pass
        if sum == num:
            print("Numero perfecto. ")
            input("\npresiona ENTER para continuar ")
        else:
            print("Numero imperfecto")
            input("\npresiona ENTER para continuar ")
    elif seleccion == 0:
        print("gracias por usar nuestro sistema")
    else:
        print("Por favor dijite un valor valido")
        input("\npresiona ENTER para continuar ")
        continue
    