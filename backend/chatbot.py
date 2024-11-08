import re
import random

def contact_preference_response(user_input, contact_choice):

    if contact_choice == "1":
        return "Perfecto, te contactaremos por teléfono. ¿Cuál es tu número?"
    elif contact_choice == "2":
        return "Genial, te contactaremos por correo electrónico. ¿Cuál es tu dirección de correo?"
    elif contact_choice == "3":
        return "Está bien, te contactaremos por mensaje de texto. ¿Cuál es tu número?"
    else:
        return "Lo siento, no entiendo esa opción. Por favor elige 1, 2 o 3."

def get_response(user_input):

    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_message(split_message)
    if response=="":
        response=unknown()
    return {"response": response}

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    """
    Calcula la probabilidad de que un mensaje del usuario contenga palabras reconocidas.

    Args:
    user_message (list): Lista de palabras del mensaje del usuario.
    recognized_words (list): Palabras que el bot reconoce.
    single_response (bool): Indica si se debe dar una respuesta única.
    required_words (list): Lista de palabras requeridas para considerar el mensaje como válido.

    Returns:
    int: Probabilidad en porcentaje de que el mensaje coincida con la respuesta esperada.
    """
    message_certainty = 0
    has_required_words = True

    # Cuenta palabras reconocidas en el mensaje del usuario
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    # Calcula el porcentaje de coincidencia
    percentage = float(message_certainty) / float(len(recognized_words))

    # Verifica que las palabras requeridas estén presentes
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_message(message):
    """
    Evalúa todas las posibles respuestas y devuelve la mejor coincidencia.

    Args:
    message (list): Lista de palabras del mensaje del usuario.

    Returns:
    str: Respuesta del bot basada en la mayor probabilidad.
    """
    highest_prob = {}
    global contact_choice  # Para acceder a la opción elegida globalmente

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        """
        Agrega una respuesta y su probabilidad de coincidencia al diccionario de probabilidades.

        Args:
        bot_response (str): Respuesta del bot.
        list_of_words (list): Palabras reconocidas para esta respuesta.
        single_response (bool): Indica si se debe dar una respuesta única.
        required_words (list): Palabras requeridas para considerar la respuesta válida.
        """
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Definición de respuestas posibles
    response('Hola soy tu bot de ayuda', ['hola', 'saludos', 'buenas', 'quehubo'], single_response=True)
    response('Estoy bien, ¿y tú?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
    response('Estamos ubicados en la Avenida Calle 32 No. 17-30', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
    response('Feliz día', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
    #Preguntas iniciales
    response('¿Cuál es tu nombre?', ['nombre', 'me llamo', 'soy'], single_response=True)
    response('¿Puedes darme tu correo electrónico para poder ayudarte mejor?', ['correo', 'email', 'puedo escribir'], single_response=True)
    # Respuestas adicionales
    response('Nuestros horarios de atención son de 8 am a 5 pm.', ['horarios', 'atencion'], single_response=True)
    response('Ofrecemos diversos cursos. ¿Te gustaría saber más sobre alguno en particular?', ['cursos', 'ofrecen'], single_response=True)
    response('Puedes consultar los próximos eventos en la página web.', ['eventos', 'proximos', 'consultar'], single_response=True)
    response('Los sábados estamos cerrados, pero puedes contactarnos durante la semana.', ['sabados', 'cerrados'], single_response=True)
    response('Puedes contactarnos al teléfono 56747444 para más información.', ['telefono', 'contacto', 'llamar'], single_response=True)
    response('Para hablar con un asesor, puedes llamarnos al 56747444 o escribirnos a nuestro correo de contacto.', ['asesor', 'comunicarse', 'hablar'], single_response=True)
    response('¿Cómo te gustaría que te contactáramos? Puedes elegir: 1) Teléfono, 2) Correo electrónico, 3) Mensaje de texto.',
         ['contactar', 'como', 'medio', 'preferencia'], single_response=True)

    # Obtiene la mejor coincidencia
    best_match = max(highest_prob, key=highest_prob.get)

    return best_match if highest_prob[best_match]> 0 else ""

def unknown():
    """
    Devuelve una respuesta predeterminada cuando no hay coincidencia con el mensaje del usuario.

    Returns:
    str: Respuesta predeterminada del bot.
    """
    responses = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres decir.',
                 'Consúltalo en la página de nuestra universidad.']
    return responses[random.randrange(3)]

# Ciclo para interactuar con el bot
contact_menu_active = False  # Estado para saber si el menú de contacto está activo
contact_choice = None  # Almacena la opción de contacto elegida
#
#while True:
#    user_input = input('You: ')

    # Si el menú de contacto está activo, pide la información adicional
#    if contact_menu_active:
        # Pregunta el número o el correo según la opción elegida
#        print(contact_preference_response(user_input, contact_choice))
#        contact_menu_active = False  # Reinicia el estado después de la respuesta
#        continue
#
#    response = get_response(user_input)
#    print("Bot: " + response)

    # Si se activa el menú de contacto, guarda la opción y espera más información
#    if "contactar" in response:
#        contact_menu_active = True
        # Se almacena la opción elegida en contact_choice
#        if "1" in user_input:
#            contact_choice = "1"
#        elif "2" in user_input:
#            contact_choice = "2"
#        elif "3" in user_input:
#            contact_choice = "3"
