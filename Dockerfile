FROM python:3.12 

WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     && rm -rf /var/lib/apt/lists/*

# Сначала копируем только requirements.txt и устанавливаем зависимости
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt

# Затем копируем остальной код
COPY . /app

CMD ["python3", "server.py"]

#docker build -t server-service:latest .   

#docker run -d --name server-service -p 500:5000 server-service:latest