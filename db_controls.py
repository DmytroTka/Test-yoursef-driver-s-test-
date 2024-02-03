import sqlite3
from flask import g


def add_question(question, answer1, answer2, correct):
    msg = ''
    try:
        with sqlite3.connect('app.db') as con:
            cur = con.cursor()
            cur.execute("""INSERT INTO drivers_test
                        (question, ans1, ans2, correct) VALUES (?, ?, ?, ?)""",
                        (question, answer1, answer2, correct))
            con.commit()
            msg = 'Successfully added'
    except:
        con.rollback()
        msg = 'Error in insert operation'
    finally:
        con.close()
        return msg


def get_db():

    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("app.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM drivers_test")
        return cursor.fetchall()
        # db.close() not




'''
'''
