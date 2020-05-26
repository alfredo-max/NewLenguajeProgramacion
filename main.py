from flask import Flask,render_template,request
import grammar
from tokens import getsalidailegal,clearsalidailegal

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# esta ruta recibe el codigo del textarea
@app.route('/codigo',methods=['POST'])
def codigo():
    codigo = request.form.get("code") #guarda el codigo del text area
    grammar.cargar_codigo(codigo) #carga el codigo para analizarlo en el lexer y parser
    salidaweb=getsalidailegal()#toma los errores en la salida ilegal
    clearsalidailegal()
    return render_template('home.html',codigo=codigo ,salida=salidaweb)
    
if __name__ == '__main__':
    app.run(debug=True)  