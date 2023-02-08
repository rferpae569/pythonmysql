#FLASK_ENV=development
from flask import Flask, render_template,request
from cargar import usuarios
app = Flask(__name__)


@app.route('/') 
def inicio(): 
    return render_template('cargar.html')

@app.route('/datos')
def carga():
    a=usuarios()
    return a.datos()

@app.route('/insert', methods = ['POST'])
def insertado():
    a=usuarios()
    nom=request.form['nom']
    ape=request.form['ape']
    return a.insertar(nom,ape)
    
    
if __name__ == '__main__': 
    app.run(debug=True)
