from flask import Flask, render_template, request, redirect,session

app = Flask(__name__)
app.secret_key = 'estoessecreto'

#rutas
@app.route ('/', methods = ['GET'])
def counter():
    if 'views' in session:
        session ['views'] += 1
    else:
        session ['views'] = 0
    return render_template('index.html', views= session['views'])

@app.route ('/count2', methods = ['POST'])
def counter2():
    session ['views'] += 1
    return redirect ('/')

@app.route('/destroy_session', methods = ['GET'])
def destroy():
    if 'views' in session:
        session.clear ()
    return redirect ('/')



if __name__ == '__main__':
    app.run (debug = True)
