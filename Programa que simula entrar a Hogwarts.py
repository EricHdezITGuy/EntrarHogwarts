#Examen I parcial II cuatrimestre 2020

#Pedir la primera decision al end user
decision = input("Deseas abrir la carta? ")
if decision == "si" or decision == "Si":
    print("Has sido escogido y las clases inician el 11 de Julio. Por favor seguir las siguientes instrucciones.")

    #Declaración de variables
    barryTrotter = "Barry Trotter"
    colorRojo = int(0)
    colorVerde = int(0)
    colorAmarillo = int(0)
    colorAzul = int(0)
    varitaMagica = int(0)
    libroFantastico = int(0)
    hechizo = int(0)
    pocionRelajante = int(0)

    varitaMagica = int(input("Por favor indicar cuál varita mágica te escogió, utilizando un valor del 1 al 4: "))

    #Cálculo de la varita magica, acorde a lo que el usuario introdujo
    if varitaMagica == 1:
        colorRojo = colorRojo + 1
    elif varitaMagica == 2:
        colorVerde == colorVerde + 1
    elif varitaMagica == 3:
        colorAmarillo == colorAmarillo +1
    else:
        colorAzul: colorAzul + 1
    libroFantastico = int(input("Por favor ingresar el libro de animal fantástico que más te guste, utilizando un valor del 1 al 5: "))

    #Cálculo del libro fantastico, acorde a lo que el usuario introdujo
    if libroFantastico == 1:
        colorVerde == colorVerde + 1
    elif libroFantastico == 2:
        colorAzul == colorAzul + 1
    elif libroFantastico == 3:
        colorAmarillo == colorAmarillo + 1
    elif libroFantastico == 4:
        colorRojo == colorRojo + 1
    else:
        colorRojo == colorRojo + 1
        colorVerde == colorVerde + 1

    diaNoche = input("Por favor indicar si le gusta más el día o la noche: ")

    #Cálculo de la eleccion del dia o noche, acorde a lo que el usuario introdujo
    if diaNoche == "Dia" or "dia" or "Día" or "día":
        colorVerde == colorVerde + 1
        colorAzul == colorAzul + 1
    else:
        colorAmarillo == colorAmarillo + 1
        colorRojo == colorRojo + 1

    hechizo = int(input("Has sido atacado, por favor elige un hechizo del 1 al 4: "))

    #Cálculo del hechizo, acorde a lo que el usuario introdujo
    if hechizo == 1:
        colorVerdePorciento = colorVerde * 0.25
        colorVerde = colorVerde + colorVerdePorciento
    elif hechizo == 2:
        colorRojoPorciento = colorRojo * 0.15
        colorRojo = colorRojo + colorRojoPorciento
    elif hechizo == 3:
        colorAzulPorciento = colorAzul * 0.40
        colorAzul = colorAzul + colorAzulPorciento
    else:
        colorAmarilloPorciento = colorAmarillo * 0.10
        colorAmarillo = colorAmarillo + colorAmarilloPorciento

    pocionRelajante = int(input("Indicar qué poción va a tomar, escogiendo una opción entre el 1 al 5: "))

    #Cálculo de la poción, acorde a lo que el usuario introdujo
    if pocionRelajante == 1:
        colorAzulPorcientoNuevo = colorAzul * 0.10
        colorAzul = colorAzul + colorAzulPorcientoNuevo
        colorRojoPorcientoNuevo = colorRojo * 0.20
        colorRojo = colorRojo - colorRojoPorcientoNuevo
    elif pocionRelajante == 2:
        colorRojoPorcientoNuevo = colorRojo * 0.15
        colorRojo = colorRojo - colorRojoPorcientoNuevo
        colorVerdePorcientoNuevo = colorVerde * 0.07
        colorVerde = colorVerde + colorVerdePorcientoNuevo
        colorAmarilloPorcientoNuevo = colorAmarillo * 0.07
        colorAmarillo = colorAmarillo + colorAmarilloPorcientoNuevo
    elif pocionRelajante == 3:
        colorRojoPorcientoNuevo = colorRojo * 0.05
        colorRojo = colorRojo + colorRojoPorcientoNuevo
        colorAzulPorcientoNuevo = colorAzul * 0.05
        colorAzul = colorAzul + colorAzulPorcientoNuevo
        colorVerdePorcientoNuevo = colorVerde * 0.03
        colorVerde = colorVerde - colorVerdePorcientoNuevo
        colorAmarilloPorcientoNuevo = colorAmarillo * 0.03
        colorAmarillo = colorAmarillo - colorAmarilloPorcientoNuevo
    elif pocionRelajante == 4:
        colorRojoPorcientoNuevo = colorRojo * 0.15
        colorRojo = colorRojo - colorRojoPorcientoNuevo
        colorVerdePorcientoNuevo = colorVerde * 0.07
        colorVerde = colorVerde + colorVerdePorcientoNuevo
        colorAmarilloPorcientoNuevo = colorAmarillo * 0.07
        colorAmarillo = colorAmarillo + colorAmarilloPorcientoNuevo
    else:
        colorRojoPorcientoNuevo = colorRojo * 0.05
        colorRojo = colorRojo + colorRojoPorcientoNuevo
        colorAzulPorcientoNuevo = colorAzul * 0.05
        colorAzul = colorAzul + colorAzulPorcientoNuevo
        colorVerdePorcientoNuevo = colorVerde * 0.03
        colorVerde = colorVerde - colorVerdePorcientoNuevo
        colorAmarilloPorcientoNuevo = colorAmarillo * 0.03
        colorAmarillo = colorAmarillo - colorAmarilloPorcientoNuevo

    #Cálculo final para escoger la casa    
    if colorRojo > colorVerde or colorAmarillo or colorAzul:
        casa = "Softffindor"
    elif colorVerde > colorRojo or colorAmarillo or colorAzul:
        casa = "Teletherin"
    elif colorAzul > colorRojo or colorVerde or colorAmarillo:
        casa = "Webvenclaw"
    else:
        casa = "Ticsepuff"
    print("Felicidades",barryTrotter,"! El sombrero seleccionador dijo que tu casa será:",casa)

    #Para ver por qué tengo el mismo resultado siempre
    print(colorRojo,"/",colorVerde,"/",colorAzul,"/",colorAmarillo)
else:
    print("Perdió la oportunidad de entrar a Onwarsh, Escuela de Magia y Hechicería.")