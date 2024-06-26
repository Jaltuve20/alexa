import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import subprocess
import platform

name = 'alexa'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hola señor Leonardo")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-US")
            rec = rec.lower()
            print(rec)
            return rec
    except:
        pass
    return ""

def open_incognito(search_query):
    if platform.system() == "Windows":
        subprocess.run(['start', 'opera', '--private', f'https://www.google.com/search?q={search_query}'], shell=True)
    # Puedes agregar soporte para otros sistemas operativos si es necesario
    else:
        talk('Modo incógnito solo soportado en Windows con Opera GX')

def run():
    while True:
        rec = listen()

        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            talk('Reproduciendo' + music)
            pywhatkit.playonyt(music)

        elif 'busca' in rec:
            if 'busca en privado' in rec:
                search_query = rec.replace('busca en privado', '')
                talk('Buscando en modo incógnito ' + search_query)
                open_incognito(search_query.strip())
            else:
                search_query = rec.replace('busca', '')
                talk('Buscando en Google ' + search_query)
                url = f"https://www.google.com/search?q={search_query.strip()}"
                webbrowser.open(url)

        elif 'abre whatsapp' in rec:
            talk('Abriendo WhatsApp en el navegador')
            webbrowser.open('https://web.whatsapp.com/')
            # Puedes agregar un tiempo de espera aquí si es necesario
            # time.sleep(5)  # Espera 5 segundos antes de continuar

        elif 'abre el traductor' in rec:
            talk('Abriendo el traductor en el navegador')
            webbrowser.open('https://translate.google.com/?hl=es&tab=TT&sl=en&tl=es&op=translate')

        elif 'abre inteligencia artificial' in rec:
            talk('Abriendo ChatGPT en el navegador')
            webbrowser.open('https://chat.openai.com/')
            
run()
