def temp_baja (temperatura):
    print("la temperatura es baja")
    input("\npresiona ENTER para continuar")
def temp_normal (temperatura):
    print("la temperatura es normal")
    input("\npresiona ENTER para continuar")
def temp_alta (temperatura):
    print("\nla temperatura es alta")
    input("\npresiona ENTER para continuar")
       
def exit ():
    print("muchas gracias por usar nuestro sistema")


def menu ():
    print("1.Realizar consulta",
          "\n0. salir")
    return

print("Bienvenido al sitema de validacion de temperatura de incubacion")

while True:
    menu()
    seleccion = int(input("\npor favor dijita tu seleccion "))
    if seleccion == 1:
        temperatura = int(input("por favor ingresa la temperatura en grados centigrados "))
        if temperatura <= 26 :
            temp_baja(temperatura)
            
        elif temperatura > 34 :
            temp_alta(temperatura)
            
        else:   
            temp_normal(temperatura)
            
    elif seleccion == 0:
        
        break
    else:
        print("Por favor dijite un valor valido")
        continue
        



