from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    ahora= datetime.now()
    fecha_hora= ahora.strftime("%Y-%m-%d %H:%M:%S")
    mensaje= f"Bienvenido a la app Prueba DevOps, la fecha y hora son: {fecha_hora}"
    return render_template('index.html', mensaje = mensaje)

if __name__ == '__main__':
    app.run(port=5000)