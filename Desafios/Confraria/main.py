from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/parceiros')
def parceiros():    
    return render_template('parceiros.html')

if __name__ == '__main__':
    app.run(debug=True)