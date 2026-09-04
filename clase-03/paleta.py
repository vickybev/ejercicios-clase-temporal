paleta = []

while True:
    print("\n1. Agregar   2. Ver")
    print("3. Borrar    4. Estadísticas")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        color = input("Color: ")
        paleta.append(color)
        print("Color agregado.")

    elif opcion == "2":
        if len(paleta) == 0:
            print("La paleta está vacía.")
        else:
            for posicion in range(len(paleta)):
                print(posicion + 1, paleta[posicion])

    elif opcion == "3":
        if len(paleta) == 0:
            print("No hay colores para borrar.")
        else:
            for posicion in range(len(paleta)):
                print(posicion + 1, paleta[posicion])

            numero = int(input("Número del color que querés borrar: "))

            if numero >= 1 and numero <= len(paleta):
                borrado = paleta.pop(numero - 1)
                print("Se borró:", borrado)
            else:
                print("Ese número no existe en la paleta.")

    elif opcion == "4":
        cantidad = len(paleta)
        print("Cantidad de colores:", cantidad)

        if cantidad > 0:
            mas_largo = paleta[0]

            for color in paleta:
                if len(color) > len(mas_largo):
                    mas_largo = color

            print("Color con el nombre más largo:", mas_largo)
        else:
            print("Todavía no hay un color con el nombre más largo.")

    elif opcion == "5":
        print("Programa terminado.")
        break

    else:
        print("Opción inválida.")
