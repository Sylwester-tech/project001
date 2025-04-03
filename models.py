#ten plik jes jak biblioteka która tworzy model i ustala jego parametry
from langchain_groq import ChatGroq
#Powyższa linia jest ciakawa bo z biblioteki importujemy klasę- ChatGroq jako model to jest klasa. Rozpatrjemy go go jako szablon klasy. 
#Ten szablon jest surowy- trzeba go oprogramować.
from langchain_core.messages import HumanMessage, SystemMessage  # Importuję metody do osbługi wiadomości dla użytkownika i systemu AI
#musimy zaimportować bibliotekę os aby mieć dostęp do zmiennych środowiskowych
import os

#tworzymy funkcję get_llm()
def get_llm():
    #w ciele funkcji nic nie mamy
    #Poniżej ChatGroq to jest konstruktor klasy ChatGroq. Ten konstruktor posiada argumenty pozwalajace ustalić jaki model ma być wykorzystany i weryfikuje nasz klucz API. Klucz API trzeba wygenerować na stronie GROQa. Ten klucz musi być dodany do zmiennych środowiskowych na naszym kompie.
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.environ["GROQ_API_KEY"]
    )

#wywołuję funkcję get_llm i przypisuję do obiektu llm
llm = get_llm()

# Ustalam stałą z tekstem- ta zmienna (dokładnie to jej tekst) będzie dodany automatycznie do prompta.
SYSTEM_PROMPT = """
Jesteś pomocnym nauczycielem informatyki. 
Odpowiadaj zwięźle i wyłącznie po polsku. 
Wyjaśniaj zagadnienia używając analogii.
"""
#Musimy zastosować pędlę nieskończoną while. Bez pętli model będzie się włączał podawał jedną wiadomość i się wyłączał.
#Całe działanie modelu jest w pętli
while True:
    #Pobieram dane od użytkownika -generuję napis "TY"
    user_input = input("Ty: ")
    #Konwertuję tekst ze zmiennej user_input na małe litery. Sprwadzam ifem czy użytkownik nie podał stringa exit quit wyjście. Jeśli podał to łamię 
    # pęlę za pomocą break.
    if user_input.lower() in ["exit", "quit", "wyjście"]:
        print("Do widzenia!")
        break

    # Za pomocą metody invoke wysyłam zapytanie do modelu. Invoke posiada listę argumentów. SystemMessage ustalam jakko zmienną z tekstem. 
    response_with_system = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),  # NEW: Wiadomość systemowa
        HumanMessage(content=user_input)
    ])
    
    # Wersja BEZ systemowej wiadomości
    response_without_system = llm.invoke([
        HumanMessage(content=user_input)  # Originalna wersja bez systemowego prompta
    ])
    
    # NEW: Wizualne porównanie
    print("\n--- Z PROMPTEM SYSTEMOWYM ---")
    print("Model:", response_with_system.content)
    
    print("\n--- BEZ PROMPTU SYSTEMOWEGO ---")
    print("Model:", response_without_system.content)
    print("\n" + "="*50 + "\n")