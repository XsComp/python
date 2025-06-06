from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "shadowrootsecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    difficulty = request.form['difficulty']
    session['difficulty'] = difficulty
    session['step'] = 1
    return redirect(url_for('game'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    step = session.get('step', 1)
    difficulty = session.get('difficulty', 'easy')
    response = ""

    if request.method == 'POST':
        choice = request.form.get('choice')
        if step == 1 and choice == "scan":
            response = "Open ports: 22, 80. Weak SSH credentials found."
            session['step'] = 2
        elif step == 2 and choice == "login":
            username = request.form.get("username")
            password = request.form.get("password")
            if username == "admin" and password == "omnicore123":
                session['step'] = 3
                return redirect(url_for('result', success="true"))
            else:
                response = "Login failed."
        else:
            response = "Unknown action."

    return render_template('game.html', step=step, difficulty=difficulty, response=response)

@app.route('/result')
def result():
    success = request.args.get('success')
    return render_template('result.html', success=success)

if __name__ == '__main__':
    app.run(debug=True)
