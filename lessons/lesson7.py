import sqlite3

#дневник
connect = sqlite3.connect('user.db')
#рука и ручка
cursor = connect.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                name VARCHAR (30) NOT NULL,
                age INTEGER NOT NULL,
                hobby TEXT
                ) 
            ''')

connect.commit()


#CRUD - Create Read Update Delete

#create
def create_user(name, age, hobby):
    cursor.execute(f'''
            INSERT INTO users (age, name, hobby) VALUES ("{age}", "{name}", "{hobby}")
                   ''')
    connect.commit()
    print('пользователь добавлен')

create_user('Eldar', 28, 'секситься')

#read
def get_users(name, age, hobby):
    cursor.execute('''SELECT * FROM users''')
    data = cursor.fetchall
    print(data)
    
#update
def update_user(age,row_id):
    cursor.execute('''
                   UPDATE users SET age = ? WHERE rowid =?
                   WHERE rowid =?  '''
                   (age, row_id)
                 )
    connect.commit()
    print('возвраст обновлен')
    
#delete
def delete_user(name):
    cursor.execute('''
                   DELETE FROM users WHERE name = ?
                   ''', (name,))
    connect.commit()
    print('Пользователь удален')
    
