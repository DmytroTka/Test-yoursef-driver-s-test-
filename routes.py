from flask import Flask, render_template, url_for, redirect, request, g

import db_controls
from db_controls import add_question

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_test', methods=['GET', 'POST'])
def add_test():
    if request.method == 'POST':
        question = request.form["question"]
        answer1 = request.form["answer1"]
        answer2 = request.form["answer2"]
        correct = request.form["correct"]
        msg = add_question(question, answer1, answer2, correct)
        return msg
    return render_template('add_test.html')


@app.route('/drivers_test', methods=['GET', 'POST'])
def drivers_test():
    all_data = db_controls.get_db()
    answers = []
    if request.method == 'POST':
        answers.append(request.form['check'])
    return render_template('drivers_test.html', all_data=all_data)


@app.teardown_appcontext
def close_connection(ex):

    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
