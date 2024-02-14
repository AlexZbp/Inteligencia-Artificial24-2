from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear un chatbot y cargar el corpus
chatbot = ChatBot("Chatpot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish")  # Entrenar con el corpus en español

# Funciones para manejar consultas específicas
def get_horoscope(sign):
    # Lógica para obtener el horóscopo del día para el signo dado
    if sign == 'Acuario':
        print("🔮: ♒ Tendrás un buen día, conoceras gente" )
    elif sign == 'Piscis':
        print("🔮: ♓ Tendrás un buen día, comeras helado" )
    elif sign == 'Aries':
        print("🔮: ♈ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Tauro':
        print("🔮: ♉ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Geminis':
        print("🔮: ♊ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Cáncer':
        print("🔮: ♋ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Leo':
        print("🔮: ♌ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Virgo':
        print("🔮: ♍ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Libra':
        print("🔮: ♎ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Escorpio':
        print("🔮: ♏ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Sagitario':
        print("🔮: ♐ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Capricornio':
        print("🔮: ♑ Tendrás un buen día, hablaras con tu crush" )

    return f"¡Este es el Horóscopo de día para {sign}!"

def get_sign_description(sign):
    # Lógica para obtener la descripción del signo
    if sign == 'Acuario':
        print("🔮: ♒ Este signo de aire no es de los que se atan a ideales arbitrarios.\n "
              "A riesgo de ganarse la reputación de distantes y distanciadas, este signo analítico\n"
              "e innovador prefiere situarse al margen de la multitud en lugar de seguir al rebaño." )
    elif sign == 'Piscis':
        print("🔮: ♓ tiende a ver el mundo a través de lentes de sol color de rosa, pero su alma romántica\n "
              "se basa en un profundo sentido de la intuición, la sensibilidad y la empatía que le ayudan a\n"
              "conectar con la gente a un nivel más profundo, incluso más allá de lo que el mundo ve." )
    elif sign == 'Aries':
        print("🔮: ♈ Siempre dispuesto a lanzarse de cabeza a un desafío.\n" 
              "Esa actitud positiva hace que los contratiempos de la vida no los detengan durante mucho tiempo.\n" 
              "Para ellos siempre hay una nueva montaña que conquistar." )
    elif sign == 'Tauro':
        print("🔮: ♉ Es conocido por mantener los pies puestos en la tierra, son personas prácticas y responsables.\n" 
              "Son una constante en la vida de todos, la fiabilidad es lo que ayuda a sus amigos recurran a ellos\n" 
              "cuando las cosas se ponen difíciles.")
    elif sign == 'Geminis':
        print("🔮: ♊ Tienen una refrescante dualidad que les hace atraer a la gente como un imán.\n"
              "Inquisitivas, pero adaptables, juguetonas, pero sensibles, ¡así eres tú, Géminis!\n "
              "Tu sentido de la curiosidad por lo que el mundo tiene que ofrecerte hará que las cosas nunca sean aburridas para ti." )
    elif sign == 'Cáncer':
        print("🔮: ♋ Con un mundo emocional dictado por la pasión, la calidez y un espíritu afectuoso, es más leal que nadie.\n "
              "Es el signo más hogareño, sus seres queridos se sienten realmente en casa cuando están junto a ellos." )
    elif sign == 'Leo':
        print("🔮: ♌ Extrovertidos, alegres y teatrales, ¡nadie podría acusar a Leo de sufrir por falta de confianza!\n "
              "Ellos saben lo que quieren en la vida y no tienen reparos en conseguirlo.\n "
              "Puede que el mundo piense que les encanta ser el centro de atención, pero es obvio que las cámaras los adoran." )
    elif sign == 'Virgo':
        print("🔮: ♍ Si quieres que algo se haga, llama a cualquiera. Pero si quieres algo bien hecho, llama a un Virgo.\n "
              "Metódicos, meticulosos y detallistas hasta el extremo.\n "
              "Si el mundo es un caos, está claro que solo ellos lo pueden poner en orden." )
    elif sign == 'Libra':
         print("🔮: ♎ La armonía y la paz ocupan un lugar destacado en la carta de presentación de tu signo del zodiaco, y con razón.\n" 
               "Son conocidos por el sentido de la equidad y la justicia, que los impulsan a establecer el equilibrio en todos los aspectos de su vida." )
    elif sign == 'Escorpio':
        print("🔮: ♏ Muchos los ven como agresivos y conflictivos, pero en realidad tienen pasión por defender las causas perdidas.\n "
              "Su naturaleza profundamente apasionada significa que nunca se rendirán sin luchar." )
    elif sign == 'Sagitario':
        print("🔮: ♐ Tu búsqueda del conocimiento está destinada a llevarte a grandes lugares.\n "
              "Espíritu errante, tu personalidad inconformista no echa raíces fácilmente, no cuando todavía te queda un mundo por descubrir." )
    elif sign == 'Capricornio':
        print("🔮: ♑ Metódicos, prácticos y decididos, los Capricornio no se detienen cuando tienen un objetivo en mente.\n "
              "No les gustan las charlas triviales ni los halagos vanidosos, por lo que su círculo íntimo es pequeño pero muy leal." )

    return f"¡He consultado con los astros y esta es la Descripción tu signo {sign}!"

def get_fun_facts(sign):
    # Lógica para obtener los datos curiosos del signo
    if sign == 'Acuario':
        print("🔮: ♒ " )
    elif sign == 'Piscis':
        print("🔮: ♓  " )
    elif sign == 'Aries':
        print("🔮: ♈ " )
    elif sign == 'Tauro':
        print("🔮: ♉ " )
    elif sign == 'Geminis':
        print("🔮: ♊ " )
    elif sign == 'Cáncer':
        print("🔮: ♋ " )
    elif sign == 'Leo':
        print("🔮: ♌ " )
    elif sign == 'Virgo':
        print("🔮: ♍ " )
    elif sign == 'Libra':
        print("🔮: ♎ " )
    elif sign == 'Escorpio':
        print("🔮: ♏ " )
    elif sign == 'Sagitario':
        print("🔮: ♐ " )
    elif sign == 'Capricornio':
        print("🔮: ♑ " )

    return f"Estos son algunos datos curiosos sobre tu signo {sign}"

def get_date_range(sign):
    # Lógica para obtener el rango de fechas del signo
    if sign == 'Acuario':
        print("🔮: ♒ Del 21 de Enero al 19 de Febrero" )
    elif sign == 'Piscis':
        print("🔮: ♓ Del 20 de Febrero al 20 de Marzo" )
    elif sign == 'Aries':
        print("🔮: ♈ Del 21 de Marzo al 20 de Abril" )
    elif sign == 'Tauro':
        print("🔮: ♉ Del 21 de Abril al 21 de Mayo" )
    elif sign == 'Geminis':
        print("🔮: ♊ Del 22 de Mayo al 21 de Junio" )
    elif sign == 'Cáncer':
        print("🔮: ♋ Del 22 de Junio al 23 de Julio" )
    elif sign == 'Leo':
        print("🔮: ♌ Del 24 de Julio al 23 de Agosto" )
    elif sign == 'Virgo':
        print("🔮: ♍ Del 24 de Agosto al 23 de Septiembre" )
    elif sign == 'Libra':
        print("🔮: ♎ Del 24 de Septiembre al 23 de Octubre" )
    elif sign == 'Escorpio':
        print("🔮: ♏ Del 24 de Octubre al 22 de Noviembre" )
    elif sign == 'Sagitario':
        print("🔮: ♐ Del 23 de Noviembre al 22 de Diciembre" )
    elif sign == 'Capricornio':
        print("🔮: ♑ Del 23 de Diciembre al 20 de Enero" )

    return f"El rango de fechas para tu signo este {sign}"

def get_compatibility(sign):
    # Lógica para obtener la compatibilidad del signo
    if sign == 'Acuario':
        print("🔮: ♒ " )
    elif sign == 'Piscis':
        print("🔮: ♓  " )
    elif sign == 'Aries':
        print("🔮: ♈ " )
    elif sign == 'Tauro':
        print("🔮: ♉ " )
    elif sign == 'Geminis':
        print("🔮: ♊ " )
    elif sign == 'Cáncer':
        print("🔮: ♋ " )
    elif sign == 'Leo':
        print("🔮: ♌ " )
    elif sign == 'Virgo':
        print("🔮: ♍ " )
    elif sign == 'Libra':
        print("🔮: ♎ " )
    elif sign == 'Escorpio':
        print("🔮: ♏ " )
    elif sign == 'Sagitario':
        print("🔮: ♐ " )
    elif sign == 'Capricornio':
        print("🔮: ♑ " )

    return f"¡Según los astros el signo más compatible para ti {sign} es este !"

def get_tips(sign):
    # Lógica para obtener el consejo del día del signo
    if sign == 'Acuario':
        print("🔮: ♒ " )
    elif sign == 'Piscis':
        print("🔮: ♓ " )
    elif sign == 'Aries':
        print("🔮: ♈ " )
    elif sign == 'Tauro':
        print("🔮: ♉ " )
    elif sign == 'Geminis':
        print("🔮: ♊ " )
    elif sign == 'Cáncer':
        print("🔮: ♋ " )
    elif sign == 'Leo':
        print("🔮: ♌ " )
    elif sign == 'Virgo':
        print("🔮: ♍ " )
    elif sign == 'Libra':
        print("🔮: ♎ " )
    elif sign == 'Escorpio':
        print("🔮: ♏ " )
    elif sign == 'Sagitario':
        print("🔮: ♐ " )
    elif sign == 'Capricornio':
        print("🔮: ♑ " )

    return f"El consejo que tengo para ti {sign}, es este."

def get_chinese_horoscope(sign):
    # Lógica para obtener el horóscopo chino del signo
    if sign == 'Acuario':
        print("🔮: ♒ " )
    elif sign == 'Piscis':
        print("🔮: ♓  " )
    elif sign == 'Aries':
        print("🔮: ♈ " )
    elif sign == 'Tauro':
        print("🔮: ♉ " )
    elif sign == 'Geminis':
        print("🔮: ♊ " )
    elif sign == 'Cáncer':
        print("🔮: ♋ " )
    elif sign == 'Leo':
        print("🔮: ♌ " )
    elif sign == 'Virgo':
        print("🔮: ♍ " )
    elif sign == 'Libra':
        print("🔮: ♎ " )
    elif sign == 'Escorpio':
        print("🔮: ♏ " )
    elif sign == 'Sagitario':
        print("🔮: ♐ " )
    elif sign == 'Capricornio':
        print("🔮: ♑ " )

    return f"¡Tu horóscopo {sign} en el Horóscopo Chino fue este!"

# Condiciones de salida
exit_conditions = (":q", "quit", "exit")

# Bucle principal
while True:
    query = input("> ")

    # Verificar condiciones de salida
    if query in exit_conditions:
        break

    # Consultas específicas
    elif "horóscopo" in query.lower():
        signo = input("Ingresa tu signo: ")
        print(get_horoscope(signo))

    elif "descripción" in query.lower():
        signo = input("Ingresa tu signo: ")
        print(get_sign_description(signo))

    elif "datos curiosos" in query.lower():
        signo = input("Ingresa tu signo: ")
        print(get_fun_facts(signo))

    elif "rango de fechas" in query.lower():
        signo = input("Ingresa tu signo: ")
        print(get_date_range(signo))

    elif "compatibilidad" in query.lower():
        signo = input("Ingresa tu signo: ")
        print(get_compatibility(signo))

    elif "consejo" in query.lower():
        signo = input("Ingresa tu signo: ")
        print(get_tips(signo))

    elif "chino" in query.lower():
        signo = input("Ingresa tu signo: ")
        print(get_chinese_horoscope(signo))

    # Respuestas generales del chatbot
    else:
        response = chatbot.get_response(query)
        print(f"🔮 {response}")
