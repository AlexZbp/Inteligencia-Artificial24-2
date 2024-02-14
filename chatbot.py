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
        print("🔮: ♒ Abraza tu originalidad y autenticidad. Hoy es un buen día para destacar en tu singularidad.\n "
                    "Contribuye a causas sociales. Tu naturaleza altruista será apreciada por aquellos a tu alrededor.\n "
                    "Sé flexible en tus planes. La adaptabilidad te permitirá aprovechar nuevas oportunidades." )
    elif sign == 'Piscis':
        print("🔮: ♓ Confía en tu intuición en asuntos emocionales. La conexión emocional fortalecerá relaciones.\n "
                    "Dedica tiempo a la creatividad. La expresión artística te brindará satisfacción y liberación emocional.\n "
                    "Escucha tus sueños. Las señales intuitivas te guiarán hacia decisiones acertadas." )
    elif sign == 'Aries':
        print("🔮: ♈ La energía planetaria te impulsa a liderar hoy. Toma la iniciativa en proyectos importantes.\n "
                    "Aprovecha la creatividad que te rodea. Las ideas innovadoras te llevarán a nuevas oportunidades.\n "
                    "Enfrenta los desafíos con valentía. Tu determinación te ayudará a superar cualquier obstáculo." )
    elif sign == 'Tauro':
        print("🔮: ♉ La paciencia será clave en tus relaciones hoy. Escucha con atención antes de tomar decisiones importantes.\n "
                    "Enfócate en tus metas a largo plazo. Un enfoque constante te acercará más a tus sueños.\n "
                    "Sé flexible en tu enfoque. La adaptabilidad te permitirá sortear cualquier cambio inesperado." )
    elif sign == 'Geminis':
        print("🔮: ♊ La comunicación será tu superpoder hoy. Exprésate con claridad para evitar malentendidos.\n "
                    "Explora nuevas formas de aprendizaje. La curiosidad intelectual te abrirá puertas.\n "
                    "Mantén un equilibrio entre trabajo y diversión. La variedad te ayudará a mantener la energía positiva." )
    elif sign == 'Cáncer':
        print("🔮: ♋ Confía en tu intuición en asuntos emocionales. La sensibilidad te guiará hacia soluciones amorosas.\n "
                    "Dedica tiempo para cuidar de ti mismo. El autocuidado fortalecerá tu bienestar emocional.\n "
                    "Expresa tus sentimientos con honestidad. La autenticidad fortalecerá tus relaciones." )
    elif sign == 'Leo':
        print("🔮: ♌ Hoy es un día para brillar en el trabajo. Tu liderazgo será reconocido y apreciado.\n "
                    "La creatividad fluye a tu alrededor. Aprovecha para destacar en proyectos artísticos.\n "
                    "Mantén una actitud positiva. Tu optimismo contagioso será inspirador para los demás." )
    elif sign == 'Virgo':
        print("🔮: ♍ Enfócate en la organización y la eficiencia. Pequeños cambios tendrán grandes resultados.\n "
                    "Sé detallista en tus tareas. La precisión te garantizará el éxito en tus proyectos.\n "
                    "Busca el equilibrio entre el trabajo y el descanso. El bienestar mental es crucial hoy." )
    elif sign == 'Libra':
        print("🔮: ♎ Encuentra el equilibrio en tus relaciones. La armonía y la colaboración serán clave hoy.\n "
                    "Sé diplomático al abordar conflictos. Tu habilidad para encontrar soluciones pacíficas será destacada.\n "
                    "Dedica tiempo a la creatividad. La expresión artística te brindará satisfacción emocional." )
    elif sign == 'Escorpio':
        print("🔮: ♏ Enfrenta los desafíos con intensidad. Tu determinación te permitirá superar cualquier obstáculo.\n "
                    "Profundiza en tus relaciones personales. La conexión emocional fortalecerá lazos importantes.\n "
                    "Aprovecha tu intuición en decisiones financieras. La perspicacia te guiará hacia inversiones acertadas." )
    elif sign == 'Sagitario':
        print("🔮: ♐ Abraza la aventura y la exploración. Hoy es propicio para descubrimientos emocionantes.\n "
                    "Mantén una actitud optimista. Tu positivismo contagioso impactará positivamente en tu entorno.\n "
                    "Aprende algo nuevo. La expansión intelectual te abrirá puertas a nuevas oportunidades." )
    elif sign == 'Capricornio':
        print("🔮: ♑ Enfócate en tus responsabilidades con disciplina. Tu dedicación te acercará a tus metas.\n "
                    "Establece metas realistas. El logro de pequeños objetivos te dará un sentido de logro.\n "
                    "Sé pragmático en la toma de decisiones. La lógica será tu guía en situaciones desafiantes." )

    return f"¡Este es el Horóscopo del día para {sign}!"

def get_sign_description(sign):
    # Lógica para obtener la descripción del signo
    if sign == 'Acuario':
        print("🔮: ♒ Este signo de aire no es de los que se atan a ideales arbitrarios.\n "
              "A riesgo de ganarse la reputación de distantes y distanciadas, este signo analítico\n"
              "e innovador prefiere situarse al margen de la multitud en lugar de seguir al rebaño." )
    elif sign == 'Piscis':
        print("🔮: ♓ Tiende a ver el mundo a través de lentes de sol color de rosa, pero su alma romántica\n "
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
        print("🔮: ♒ Acuario es conocido por ser el signo más rebelde del zodiaco. Los acuarianos son personas innovadoras e independientes que valoran la libertad de pensamiento y acción. \n" 
        "A menudo se les describe como excéntricos y impredecibles, pero también son amables y humanitarios. " )
    elif sign == 'Piscis':
        print("🔮: ♓ Piscis es conocido por ser el signo más místico del zodiaco. Los piscianos son personas sensibles e intuitivas que valoran la conexión emocional y espiritual.\n "
        "A menudo se les describe como soñadores y escapistas, pero también son compasivos y creativos.  " )
    elif sign == 'Aries':
        print("🔮: ♈ Aries es el primer signo del zodiaco y por ello representa el comienzo de un nuevo ciclo. \n "
        "Este signo está asociado con la energía, la iniciativa y la acción. Los arianos son conocidos por ser valientes, \n" 
        "apasionados y decididos. Si eres Aries, es probable que tengas una personalidad fuerte y un gran sentido de la aventura." )
    elif sign == 'Tauro':
        print("🔮: ♉ Tauro es conocido por ser el signo más terco del zodiaco. Los taurinos son personas prácticas y trabajadoras que valoran \n "
        "la estabilidad y la seguridad. A menudo se les describe como obstinados y difíciles de convencer, pero también son leales y confiables. " )
    elif sign == 'Geminis':
        print("🔮: ♊ Géminis es el signo más dual del zodiaco. Los geminianos son conocidos por su habilidad para adaptarse a diferentes situaciones \n "
        "y por tener dos personalidades distintas. A veces pueden ser divertidos y sociables, mientras que otras veces pueden ser reservados y solitarios. " )
    elif sign == 'Cáncer':
        print("🔮: ♋ Cáncer es conocido por ser el signo más emocional del zodiaco. Los cancerianos son personas sensibles y empáticas que valoran las relaciones \n "
        "íntimas y el hogar. A menudo se les describe como emocionales y melancólicos, pero también son protectores y leales. " )
    elif sign == 'Leo':
        print("🔮: ♌ Leo es conocido por ser el signo más vanidoso del zodiaco. Los leoninos son personas seguras de sí mismas y ambiciosas que valoran la atención \n "
        "y el reconocimiento. A menudo se les describe como arrogantes y egocéntricos, pero también son generosos y leales. " )
    elif sign == 'Virgo':
        print("🔮: ♍ Virgo es conocido por ser el signo más perfeccionista del zodiaco. Los virginianos son personas organizadas y detallistas que valoran la precisión y \n "
        "la eficiencia. A menudo se les describe como críticos y exigentes, pero también son trabajadores y dedicados. " )
    elif sign == 'Libra':
        print("🔮: ♎ Libra es conocido por ser el signo más equilibrado del zodiaco. Los librianos son personas pacíficas y armoniosas que valoran la justicia y la igualdad. \n "
        "A menudo se les describe como diplomáticos y amables, pero también pueden ser indecisos y evasivos. " )
    elif sign == 'Escorpio':
        print("🔮: ♏  Escorpio es conocido por ser el signo más intenso del zodiaco. Los escorpianos son personas apasionadas y misteriosas que valoran la profundidad emocional \n "
        "y la transformación personal. A menudo se les describe como celosos y posesivos, pero también son leales y comprometidos." )
    elif sign == 'Sagitario':
        print("🔮: ♐ Sagitario es conocido por ser el signo más aventurero del zodiaco. Los sagitarianos son personas optimistas y entusiastas que valoran la libertad y la exploración.\n "
        "A menudo se les describe como imprudentes y arrogantes, pero también son sinceros y generosos. " )
    elif sign == 'Capricornio':
        print("🔮: ♑ Capricornio es conocido por ser el signo más ambicioso del zodiaco. Los capricornianos son personas trabajadoras y disciplinadas que valoran el éxito y el logro personal. \n "
        "A menudo se les describe como fríos y distantes, pero también son leales y responsables. " )

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
        print("🔮: ♒ Cáncer y Tauro " )
    elif sign == 'Piscis':
        print("🔮: ♓  Géminis, Sagitario y Leo " )
    elif sign == 'Aries':
        print("🔮: ♈ Géminis, Acuario, Leo y Tauro" )
    elif sign == 'Tauro':
        print("🔮: ♉ Capricornio, Piscis y Virgo " )
    elif sign == 'Geminis':
        print("🔮: ♊ Acuario y Libra " )
    elif sign == 'Cáncer':
        print("🔮: ♋ Virgo, Escorpio y Tauro " )
    elif sign == 'Leo':
        print("🔮: ♌ Libra, Sagitario y Aries" )
    elif sign == 'Virgo':
        print("🔮: ♍ Cáncer, Tauro y Capricornio " )
    elif sign == 'Libra':
        print("🔮: ♎ Leo y Sagitario " )
    elif sign == 'Escorpio':
        print("🔮: ♏ Cáncer, Piscis y Capricornio " )
    elif sign == 'Sagitario':
        print("🔮: ♐ Acuario y Libra " )
    elif sign == 'Capricornio':
        print("🔮: ♑ Tauro, Virgo y Escorpio " )

    return f"¡Según los astros el signo más compatible para ti {sign} es este !"

def get_tips(sign):
    # Lógica para obtener el consejo del día del signo
    if sign == 'Acuario':
        print("🔮: ♒ ¡Amas con intensidad! Pero el orgullo se interpone y no te deja expresar tus sentimientos. ¡Para! Estás arruinando el mejor momento que la vida te regala para amar y alejas a quien está cerca de ti. ¡Los astros de llenas de calma y te incitan a dar rienda suelta a lo que sientes!" )
    elif sign == 'Piscis':
        print("🔮: ♓ Te dejas contagiar por la magia del romance que inunda el ambiente. ¡Abres tu corazón y bajas la guardia! Cupido llega con todas sus flechas y no te deja salida. ¡Te conquista un amor inesperado! Los astros te llenan de energía positiva y facilitan la expresión de sentimientos." )
    elif sign == 'Aries':
        print("🔮: ♈ La magia del romance está en el aire y por más que te resistas su aroma te alcanza. ¡Por fin tomas en serio los asuntos del corazón!  Es posible que encuentres a esa persona que tanto anhelas y que ella corresponda tus anhelos." )
    elif sign == 'Tauro':
        print("🔮: ♉ El amor que creías dormido se despierta y vuelve la pasión a tu vida. Mantén tu mira en el futuro cercano, es allí donde encuentras a la persona que llena tus expectativas. " )
    elif sign == 'Geminis':
        print("🔮: ♊ El romance te golpea con todas sus fuerzas y es posible que inicies más de un romance.¡Cuidado! Procura no meterte en relaciones establecidas donde tú seas el tercero. " )
    elif sign == 'Cáncer':
        print("🔮: ♋ Tu jovialidad y encanto hoy se redoblan. El romance y la aventura en el amor están a la orden del día y te sientes atraído por más de una persona. No tomes decisiones que impliquen compromisos sentimentales con otras personas ¡Todo es pasajero! " )
    elif sign == 'Leo':
        print("🔮: ♌ ¡Vienes de una gran decepción en el amor! Cupido se empeña en sacarte de ella y logra que la magia del romance te atrape y por fin desees volver a ver a esa persona que lleva mucho tiempo esperando una oportunidad de tu parte. " )
    elif sign == 'Virgo':
        print("🔮: ♍ La estabilidad en el amor se fortalece en este día y comienza una etapa de armonía y goce pleno. Deja que la magia del romance te contagie y crea una gran experiencia de amor para tu persona favorita. ¡Los astros te permiten dejar atrás tu timidez!" )
    elif sign == 'Libra':
        print("🔮: ♎ ¡Busca en este día el equilibrio en el amor! Cupido se acerca a la persona que te interesa y la toca con todas sus flechas. ¡Comienza un gran romance  que trasforma completamente la forma que tienes de ver la vida y el amor! " )
    elif sign == 'Escorpio':
        print("🔮: ♏ ¡Deja de esconderte! Aunque corras, Cupido te atrapa y te hace enfrentar a la persona amada. ¡Expresa todos tus sentimientos y apuéstale toda tu  energía al amor! Comienza una etapa en que los astros fortalecen tu empatía y capacidad para conectar con los demás." )
    elif sign == 'Sagitario':
        print("🔮: ♐ Un amor termina, pero Cupido hace que inicies otro que no esperabas. ¡Te sorprende la rapidez con la que te conectas y lo dispuesto que te encuentras a comprometerte nuevamente! Es la magia del romance que hoy está por todas partes. ¡Los astros fortalecen tu autoestima y te dan confianza!" )
    elif sign == 'Capricornio':
        print("🔮: ♑ Huye de las flechas de Cupido si no quieres quedar atrapado en un triángulo amoroso. Éste es un gran día para establecer compromisos serios en el campo sentimental. ¡Siempre que seas sincero! Los astros aumentan tu intuición y te alertan sobre situaciones que no sean positivas para ti." )

    return f"El consejo que tengo para ti {sign}, es este."

def get_chinese_horoscope(año):
    # Lógica para obtener el horóscopo chino del signo
    if año in ['1923', '1935', '1947', '1959', '1971', '1983', '1995', '2007', '2019', '2031']:
        print("🔮: Rata")
    elif año in ['1924', '1936', '1948', '1960', '1972', '1984', '1996', '2008', '2020', '2032']:
        print("🔮: Buey")
    elif año in ['1925', '1937', '1949', '1961', '1973', '1985', '1997', '2009', '2021', '2033']:
        print("🔮: Tigre")
    elif año in ['1926', '1938', '1950', '1962', '1974', '1986', '1998', '2010', '2022', '2034']:
        print("🔮: Conejo")
    elif año in ['1927', '1939', '1951', '1963', '1975', '1987', '1999', '2011', '2023', '2035']:
        print("🔮: Dragón")
    elif año in ['1928', '1940', '1952', '1964', '1976', '1988', '2000', '2012', '2024', '2036']:
        print("🔮: Serpiente")
    elif año in ['1929', '1941', '1953', '1965', '1977', '1989', '2001', '2013', '2025', '2037']:
        print("🔮: Caballo")
    elif año in ['1930', '1942', '1954', '1966', '1978', '1990', '2002', '2014', '2026', '2038']:
        print("🔮: Cabra")
    elif año in ['1931', '1943', '1955', '1967', '1979', '1991', '2003', '2015', '2027', '2039']:
        print("🔮: Mono")
    elif año in ['1932', '1944', '1956', '1968', '1980', '1992', '2004', '2016', '2028', '2040']:
        print("🔮: Gallo")
    elif año in ['1933', '1945', '1957', '1969', '1981', '1993', '2005', '2017', '2029', '2041']:
        print("🔮: Perro")
    elif año in ['1934', '1946', '1958', '1970', '1982', '1994', '2006', '2018', '2030', '2042']:
        print("🔮: Cerdo")
    else:
        print("¡Año no válido!")

    return f"El animal para el año {año} segun el horoscopo chino es este."

    # Función para mostrar las opciones disponibles
def show_options():
    print(" 🔮 Bienvenido al Botroscopo, puedes preguntarme sobre:")
    print("- El horóscopo del día, solo pon horóscopo")
    print("- La descripción de un signo zodiacal, solo pon descripción.")
    print("- Algunos datos curiosos de un signo zodiacal, solo pon datos curiosos.")
    print("- El rango de fechas de un signo zodiacal, solo pon rango de fechas.")
    print("- La compatibilidad de un signo con otros, solo pon compatibilidad.")
    print("- Algún consejo para tu signo zodiacal, solo pon consejo.")
    print("- El animal de signo tu zodiacal en el horóscopo chino, solo pon chino.")
    print("- Para salir escribe: exit, q o quit.")
    print(" 🔮 Por favor escribe tu signo con mayúscula y escribe los acentos 🔮")
    


# Condiciones de salida
exit_conditions = (":q", "quit", "exit")

# Bucle principal
while True:
    query = input("> ")

    # Verificar condiciones de salida
    if query in exit_conditions:
        break

    # Muestra las opciones al usuario 
    elif "opciones" in query.lower():
        show_options()

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
        animal = input("Ingresa tu año de nacimiento: ")
        print(get_chinese_horoscope(animal))

    # Respuestas generales del chatbot
    else:
        response = chatbot.get_response(query)
        print(f"🔮 {response}")
