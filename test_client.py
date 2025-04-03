from models import get_llm

llm = get_llm()
response = llm.invoke([("human", "Cześć, jak się masz?")])
print("Odpowiedź modelu:", response.content)