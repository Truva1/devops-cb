FROM python:3.9.18-alpine
WORKDIR /app
ADD . /app

# instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

#Variable de entrono para ejecutar flask
ENV FLASK_APP=app.py

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0", "--port=5000" ]