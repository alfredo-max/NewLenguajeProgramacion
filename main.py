from flask import Flask,render_template
import grammar
from tokens import getsalida

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/codigo',methods=['POST'])
def codigo():
    grammar.cargar_codigo()
    salidaweb=getsalida()
    return render_template('home.html',salida=salidaweb)
    
if __name__ == '__main__':
    app.run(debug=True)  