from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mostrar_saida():
    with open('saida.txt', 'r') as file:
        saida = file.read()
    return render_template('saida.html', saida=saida)

if __name__ == '__main__':
    app.run(debug=True)