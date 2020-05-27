from flask import Flask,render_template,request
import grammar
from tokens import get_caracter_ilegal,clear_caracter_ilegal

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# esta ruta recibe el codigo del textarea
@app.route('/codigo',methods=['POST'])
def codigo():
    codigo = request.form.get("code") #guarda el codigo del text area
    codigo=codigo.replace("\r"," ")
    grammar.cargar_codigo(codigo) #carga el codigo para analizarlo en el lexer y parser
    caracterIlegal=get_caracter_ilegal()#toma los errores en la salida ilegal
    clear_caracter_ilegal()#limipia la info de los caracteres ilegales
    gramaerror=grammar.get_gramaticaerror()
    grammar.clear_gramaticaerror()
    return render_template('home.html',codigo=codigo ,salida=caracterIlegal,gramaerror=gramaerror)
    
if __name__ == '__main__':
    app.run(debug=True)  