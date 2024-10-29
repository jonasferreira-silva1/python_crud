# Use a imagem base do Python
FROM python:3.9-slim

# Instale dependências de sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    gcc

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie todos os arquivos para o diretório de trabalho
COPY . /app

# Instale as dependências Python
RUN pip install --upgrade pip
RUN pip install flask flask_sqlalchemy mysqlclient mysql-connector-python

# Exponha a porta 80
EXPOSE 80

# Comando para rodar o aplicativo
CMD ["python", "training.py"]
