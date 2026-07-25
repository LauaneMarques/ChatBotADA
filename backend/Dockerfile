FROM python:3.8-slim

WORKDIR /app

# Instala dependências do sistema necessárias para compilar pacotes
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Dá permissão de execução para o script de inicialização
RUN chmod +x start.sh

EXPOSE 5005

CMD ["./start.sh"]