import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio=r.listen(source)
    query=r.recognize_google(audio)
    query=query.lower()
    print(query)
    def morse(element):
        mydict={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.',
                'f':'..-.','g':'--.','h':'....','i':'..','j':'.---',
                'k':'-.-','l':'.-..','m':'--','n':'-.','o':'---',
                'p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-',
                'u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--',
                'z':'--..',' ':'/'}
        return mydict.get(element)
for element in query:
    print(morse(element),end=' ')