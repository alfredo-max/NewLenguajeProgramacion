from flask import Flask,render_template,request
import grammar
from tokens import getsalida

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/codigo',methods=['POST'])
def codigo():
    codigo = request.form.get("code")
    grammar.cargar_codigo(codigo)
    salidaweb=getsalida()
    return render_template('home.html',codigo=codigo ,salida=salidaweb)
    
if __name__ == '__main__':
    app.run(debug=True)  