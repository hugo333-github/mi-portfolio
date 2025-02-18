from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre-mi')
def sobre_mi():
    return render_template('sobre_mi.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/curriculum')
def curriculum():
    return render_template('curriculum.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    enviado = False
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Aquí puedes procesar el mensaje (enviarlo por email, guardarlo en una base de datos, etc.)
        print(f'📩 Nuevo mensaje de {nombre} ({email}): {mensaje}')
        
        enviado = True  # Activamos la variable para mostrar la alerta

    return render_template('contacto.html', enviado=enviado)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
