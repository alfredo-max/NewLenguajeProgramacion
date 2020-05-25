from flask import Flask,render_template
import grammar
app = Flask(__name__)

salida=""
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/codigo',methods=['POST'])
def codigo():
    salida=grammar.cargar_codigo()
    return render_template('mostrar.html',salida=salida)
    

if __name__ == '__main__':
    app.run(debug=True)  