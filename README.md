# Teste Finch

# Sobre o Projeto
    Este projeto tem como objetivo satisfazer os requisitos do teste tecnico para
    Analista Desenvolvedor Back End Pleno- Python da Finch

# Requisitos:
    Tenha as seguintes ferraments instaladas na distribuição Linux:
    
    1. GIT
    2. Docker
    3. Docker Compose

# Tecnologias Utilizadas

    1. Python 3.10
        
        Frameworks:
            Flask (Interface Web e APIs)
        
        Libraries:
            python-dotenv
            itsdangerous
            pika
            requests
            schedule
            pypdf2
            openpyxl
    
    2. RabbitMQ 3 Management

    3. Docker
    
    4. Docker Compose

# Instalação

    Siga as etapas abaixo para configurar e executar o projeto localmente:

    1. Clones este repositório:
        git clone https://github.com/NegaoDoTi/teste_finch
    
    2. Navegue para o diretório do projeto:
        cd test_finch
    
    3. Faça o build dos serviços utilizando docker compose:
        docker-compose build --no-cache

    4. Inicie os serviços:
        docker-compose up

# Como usar

    1. Abra seu navegador acesse http://localhost:5000/
    2. Efetue o upload dos 5 arquivos PDF
    3. Acesse http://localhost:15672/#/ para visualizar as informações da mensagens publicadas
    4. Apos fazer o upload sera informado na tela a pasta aonde os dados dos PDF seram extraídos!
    5. Para utilizar a Rota de download dos pdf deve ser informado o token no header da requisição, este token expira em 24 horas, este token e responsavel por permitir o download do arquivo na API

# Observação

    Rotas do projeto:
        http://localhost:5000/
        http://localhost:5000/upload/pdfs
        http://localhost:5000/download/<nome_arquivo_pdf.pdf>

    Fila no rabbit: download_processos

    O arquivo .env só esta no repositório remoto para facilitar e ficar mais pratico para o analisador do teste técnico.

# Pasta do projeto:

    /web Pasta aonde fica o codigo da API
    /pdf_reader Pasta aonde fica o codigo que extrai as informações dos PDFs