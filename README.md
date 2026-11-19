# Agente de IA - Oficina Mecânica

Agente conversacional desenvolvido em Python utilizando **Ollama** e o modelo **Llama 3.2** para o atendimento automatizado de clientes e fornecedores de uma oficina mecânica.

##  Funcionalidades

* **Memória de Conversa:** Mantém o histórico completo da sessão para responder perguntas com contexto.
* **Respostas em Tempo Real (Streaming):** Exibe o texto palavra por palavra à medida que o modelo gera a resposta.
* **Multilíngue:** Identifica e responde automaticamente no mesmo idioma utilizado pelo usuário.
* **Execução 100% Local:** Roda localmente via Ollama, garantindo privacidade e zero custo de API.

##  Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

1. [Python 3.10+](https://www.python.org/downloads/)
2. [Ollama](https://ollama.com/) instalado e em execução no sistema.
3. Modelo `llama3.2` baixado localmente:
   ```bash
   ollama pull llama3.2
   ```

##  Como executar o projeto

1. **Clone ou baixe este repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/Meu_agente_IA.git](https://github.com/seu-usuario/Meu_agente_IA.git)
   cd Meu_agente_IA
   ```

2. **Crie e ative um ambiente virtual (`.venv`):**
   * **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o agente:**
   ```bash
   python Agente_IA.py
   ```

Para encerrar o atendimento a qualquer momento, digite `Sair`.
