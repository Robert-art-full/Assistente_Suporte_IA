import os
from groq import Groq
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Inicializar cliente Groq
client = Groq(api_key=api_key)

# Mensagem inicial do sistema
messages = [
    {
        "role": "system",
        "content": "Você é um assistente de suporte técnico. Responda de forma clara e objetiva."
    }
]

print("Assistente de Suporte Técnico iniciado! Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("Encerrando assistente...")
        break

    # Adiciona a pergunta do usuário
    messages.append({"role": "user", "content": user_input})

    # Chamada ao Groq
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    # Pega a resposta do assistente
    answer = chat_completion.choices[0].message.content
    print(f"Assistente: {answer}\n")

    # Adiciona a resposta às mensagens (para contexto das próximas perguntas)
    messages.append({"role": "assistant", "content": answer})
