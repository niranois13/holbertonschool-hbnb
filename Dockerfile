FROM python:3.11

RUN apt-get update && apt-get upgrade -y && useradd -ms /bin/bash user
USER user
WORKDIR /home/HBnB

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8080

ENTRYPOINT [ "python", "/home/HBnB/app/app.py" ]