import sqlite3

connect = sqlite3.connect('lessons/python files/user_grade.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(30) NOT NULL)
               ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS grade (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               grade INTEGER NOT NULL,
               subject VARCHAR(30) NOT NULL,
               student_id INTEGER NOT NULL,
               FOREIGN KEY(student_id) REFERENCES students(id))
               ''')
connect.commit

def create_make_data():
    cursor.executemany(
        'INSERT INTO students(name) VALUES (?)',
        [
            ('PIDOR',),
            ('TY',),
            ('NET',),
            ('NE',),
            ('YA',),
            
        ]
    )
    connect.commit()

# create_make_data()

def create_make_grade():
    cursor.executemany(
        'INSERT INTO grade(grade, subject, student_id) VALUES (?, ?, ?)',
        [
            (5, 'algebra', 3),
            (4, 'russki', 2),
            (2, 'geometry',4),
            (1, 'fizra', 1),
            (3, 'opg', 5),
            
        ]
    )
    connect.commit()

# create_make_grade()

def get_student_grade():
    cursor.execute('''
                   SELECT students.name , grade.grade, grade.subject
                   FROM students INNER JOIN grade ON students.id = grade.student_id
                   ''')
    data = cursor.fetchall()
    
    for i in data:
        print(data)
        print(f' name: {i[0]}, GRADE: {i[1]}, subject: {i[2]}')
        
# get_student_grade()