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
        print("🔮: ♒ Tendrás un buen día, conoceras gente" )
    elif sign == 'Piscis':
        print("🔮: ♓ Eres un amor de persona pero te enojas con facilidad" )
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
         print("🔮 Eres un libro abierto, con tu carisma puedes ganarte a muchas personas" )
    elif sign == 'Escorpio':
        print("🔮: ♏ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Sagitario':
        print("🔮: ♐ Tendrás un buen día, hablaras con tu crush" )
    elif sign == 'Capricornio':
        print("🔮: ♑ Tendrás un buen día, hablaras con tu crush" )

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

    elif "horóscopo chino" in query.lower():
        signo = input("Ingresa tu signo: ")
        print(get_chinese_horoscope(signo))

    # Respuestas generales del chatbot
    else:
        response = chatbot.get_response(query)
        print(f"🔮 {response}")
