# Projeto WebSocket em Python

Este projeto demonstra a utilização de WebSocket com um servidor e um cliente em Python.

## Configuração do Ambiente

### Requisitos

- Python 3.6 ou superior
- `pip` (gerenciador de pacotes do Python)

### Passos para Configurar o Ambiente

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/seu_usuario/seu_projeto.git
    cd seu_projeto
    ```

2. **Crie um ambiente virtual**:

    ```bash
    python -m venv webEnv
    ```

3. **Ative o ambiente virtual**:
    - No Windows:
        ```bash
        webEnv\Scripts\activate
        ```
    - No macOS e Linux:
        ```bash
        source webEnv/bin/activate
        ```

4. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Execute o servidor**:

    ```bash
    python server.py
    ```

6. **Em outra janela do terminal, ative o ambiente virtual e execute o cliente**:

    ```bash
    python client.py
    ```

Seguindo esses passos, você terá o ambiente configurado corretamente para rodar o projeto WebSocket.
