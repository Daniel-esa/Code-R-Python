import random
import sqlite3

# create database in memory
db = sqlite3.connect(':memory:')

# # create database into directory
# db = sqlite3.connect("./data/test.db")

# get a cursor object
cursor = db.cursor()
# DROP TABLE
cursor.execute("""DROP TABLE IF EXISTS users""")

# CREATE TABLE
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    phone TEXT,
                    email TEXT unique,
                    password TEXT
            )"""
)

db.commit()
#Inserting (INSERT) Data into the Database
name = 'Halim'
phone = "01234567890"
email = "halim@email.com"
password = "ha1234"
cursor.execute(
    """INSERT INTO users(name, phone, email, password) VALUES (?,?,?,?)""",
    (name, phone, email, password),
)
db.commit()

name = "Alim"
phone = "01234567890"
email = "alim@email.com"
password = "al1234"
cursor.execute(
    """INSERT INTO users(name, phone, email, password) VALUES (:name, :phone, :email, :password)""",
    {
        "name": name,
        "phone": phone,
        "email": email,
        "password": password,
    },
)
db.commit()

# use list of users for inserting multiple user info
users = [
    (
        "Name " + str(i),
        str(random.randint(10000000, 1000000000)),
        "name" + str(i) + "@email.com",
        str(random.randint(10000, 90000)),
    )
    for i in range(10)
]
print(users)
cursor.executemany(
    """INSERT INTO users(name, phone, email, password) VALUES (?, ?, ?, ?)""", users
)
db.commit()


# get last row id:
print(f"last row id: {cursor.lastrowid}")

# Inserting (INSERT) Data into the Database
cursor.execute("""SELECT name, phone, email FROM users""")
user1 = cursor.fetchone()
print(user1)

user_many = cursor.fetchmany(5)
print(user_many)

user_all = cursor.fetchall()
print(user_all)

cursor.execute("""SELECT name, email, phone FROM users""")
for row in cursor:
    print(f"name: {row[0]} email: {row[1]}, phone: {row[2]}")
    
user_id = 5
cursor.execute("""SELECT name, email, phone FROM users WHERE id=?""", (user_id,))
print(cursor.fetchone())

# Updating (UPDATE) and Deleting (DELETE) Data

# update user phone with id = 5
cursor.execute("""UPDATE users SET phone = ? WHERE id = ?""", ("01710567890", user_id))
db.commit()

# delete user row with id = 8
cursor.execute("""DELETE FROM users WHERE id = ?""", (8,))
db.commit()

# Using SQLite Transactions

# update user phone with id = 5
cursor.execute("""UPDATE users SET phone = ? WHERE id = ?""", ("01712567890", user_id))

db.rollback()
cursor.execute("""SELECT name, email, phone FROM users WHERE id=2""")
print(cursor.fetchall())

#Exceptions de la base de données SQLite
#Pour les meilleures pratiques, entourez toujours les opérations 
# de base de données avec une clause try ou un gestionnaire de contexte.

# Erreur de vérification d'intégrité
# Nous pouvons utiliser l'objet Connection comme gestionnaire de contexte*
# pour valider ou annuler automatiquement les transactions
cursor.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type='table'
                 """)
print(cursor.fetchall())

db.row_factory = sqlite3.Row

cursor.execute("""SELECT name, email, phone FROM users""")

for row in cursor:

    print(f"name : {row[0]}, email: {row[1]}, phone: {row[2]}")

# close database connection
db.close()

import sys
print(sys.executable)
