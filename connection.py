import sqlite3

connection = sqlite3.connect('app.db')
connection.execute('CREATE TABLE drivers_test(question TEXT, ans1 TEXT, ans2 TEXT, correct TEXT)')
print('table was created')
connection.close()
