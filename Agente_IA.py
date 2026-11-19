import ollama

instrucao = (
    "Você é um agente de IA específico para atender os nossos clientes e fornecedores "
    "da oficina mecânica. Seja cordial, objetivo e responda sempre no mesmo idioma "
    "em que o usuário escrever."
)

# 1. Criamos a lista de mensagens fora do loop para manter o histórico na memória
historico_mensagens = [
    {"role": "system", "content": instrucao}
]

print("Agente Pronto! Digite 'Sair' para encerrarmos a aplicação.")

while True:
    pergunta = input("\nVocê: ")
    
    # Validação flexível para encerrar (aceita 'sair', 'Sair', 'SAIR', etc.)
    if pergunta.strip().lower() == "sair":
        print("Encerrando o atendimento. Até logo!")
        break

    # Adiciona a pergunta do usuário ao histórico
    historico_mensagens.append({"role": "user", "content": pergunta})

    print("Agente: ", end="", flush=True)
    
    # 2. Ativa o stream=True e envia todo o histórico acumulado
    fluxo_resposta = ollama.chat(
        model="llama3.2",
        messages=historico_mensagens,
        stream=True,
    )

    resposta_completa = ""
    for pedaco in fluxo_resposta:
        conteudo = pedaco["message"]["content"]
        print(conteudo, end="", flush=True)
        resposta_completa += conteudo

    print()  # Pula uma linha ao finalizar a resposta

    # 3. Salva a resposta completa do agente no histórico para a próxima interação
    historico_mensagens.append({"role": "assistant", "content": resposta_completa})