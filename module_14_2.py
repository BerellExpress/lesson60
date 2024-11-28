import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#for i in range(1,11):
#   cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (f"newuser{i}", f"{i}ex@gmail.com", f"{i*10}", "1000"))

#cursor.execute("UPDATE Users SET balance = 500 WHERE rowid % 2 = 1")

#cursor.execute("DELETE FROM Users WHERE rowid % 3 = 1")

#cursor.execute("SELECT username, email, COALESCE(age, 0) AS age, balance FROM Users WHERE age IS NOT 60")

#users = cursor.fetchall()
#for user in users:
   #username, email, age, balance = user
   #print(f"{username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]


cursor.execute("SELECT SUM(balance) FROM Users ")
all_balances = cursor.fetchone()[0]


print(all_balances / total_users)

connection.commit()
connection.close()