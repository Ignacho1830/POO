from Personaje_clase import Personaje

menu = """
*******************************************
* 1- Crear Personaje                      *
* 2- Jugar                                *
* 3- Salir                                *
*******************************************
"""

personajes = []  
contador = 0

while True:
    print(menu)
    opcion = int(input("Ingrese una de las opciones: "))
    
    if opcion == 1:
        nombre = input("Introduce el nombre de tu personaje: ")  
        altura = int(input("Introduce la altura de tu personaje en (cm): "))
        velocidad = int(input("Introduce la velocidad de tu personaje: "))
        resistencia = int(input("Introduce la resistencia de tu personaje: "))
        fuerza = int(input("Introduce la fuerza de tu personaje: "))
        debilidad = input("Introduce la debilidad de tu personaje: ")  

        nuevo_personaje = Personaje(nombre, altura, velocidad, resistencia, fuerza, debilidad)
        contador = contador +1

        personajes.append(nuevo_personaje)
        print(f"Personaje {nombre} creado exitosamente.\n")
    
    elif opcion == 2:
        if len(personajes) < 2:
            print("Debes crear al menos dos personajes para jugar.\n")
        else:
            p1, p2 = personajes[0], personajes[1]
            while p1.estado == "vivo" and p2.estado == "vivo":
                p2.recibir_dano(p1.atacar())
                if p2.estado == "muerto":
                    print(f"{p2.nombre} ha sido derrotado.\n")
                    break
                p1.recibir_dano(p2.atacar())
                if p1.estado == "muerto":
                    print(f"{p1.nombre} ha sido derrotado.\n")
                    break
            print("¡El juego ha terminado!\n")
            break

    

