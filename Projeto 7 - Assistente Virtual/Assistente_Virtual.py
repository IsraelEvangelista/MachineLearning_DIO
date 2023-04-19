import speech_recognition as sr
import datetime
import webbrowser
import pyttsx3
import sounddevice as sd
import wikipedia

def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 1000

    with sd.InputStream() as source:
        print('Ouvindo...')
        audio = source.read(int(5 * r.sample_rate))

        try:
            print("Reconhecendo...")
            Query = r.recognize_google(audio, language='pt-br')
            print("O comando é:", Query)

        except Exception as e:
            print(e)
            print("Repita, por favor")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Segunda-feira', 2: 'Terça-feira',
                3: 'Quarta-feira', 4: 'Quinta-feira',
                5: 'Sexta-feira', 6: 'Sábado',
                7: 'Domingo'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Hoje é " + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("A hora atual é " + hour + " horas e " + min + " minutos")


def Hello():
    speak("Olá, sou sua assistente de desktop. Em que posso ajudar? ")


def Take_query():
    Hello()
    while(True):
        query = takeCommand().lower()
        if "abrir youtube" in query:
            speak("Abrindo o Youtube")
            webbrowser.open("www.youtube.com")
        elif "métodos" in query:
            speak("Estes são os métodos disponíveis:")
            speak("Método número 1: tellDay()")
            speak("Método número 2: tellTime()")
            speak("Método número 3: Hello()")
            speak("Método número 4: Take_query()")
        elif "método número 1" in query:
            tellDay()
        elif "método número 2" in query:
            tellTime()
        elif "método número 3" in query:
            Hello()
        elif "método número 4" in query:
            Take_query()
        elif "tchau" in query:
            speak("Tchau, tenha um bom dia.")
            break
        else:
            speak("Desculpe, não entendi. Pode repetir, por favor?")


if __name__ == "__main__":
    Take_query()
