import psycopg2

conn = psycopg2.connect(
    dbname="cos102_db",
    user="postgres",
    password="cos101",
    host="localhost"
)
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS TeamMembers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    division TEXT NOT NULL,
    age INTEGER,
    module INTEGER
)''')


cursor.execute('''INSERT INTO TeamMembers (name, division, age, module) VALUES
    ('Oyinda Aina', 'Business',  32, 1),
    ('Wale Eseyin','Engineering',28, 3),
    ('Khadijah Abu','Product',   30, 2),
    ('Onyekachi Mbaike','Design',37, 5),
    ('Seike Ibojo','Growth',      33, 4),
    ('Opemipo Aikomo','Design',  28, 1),
    ('Ezra Olubi','Product',     30, 3),
    ('Alexander Fasoro','Engineering',35,1),
    ('Stephen Amaza','Growth',   40, 2),
    ('Loknan Nanyak','Loknan Nanyak',44  , 5),
    ('Ibrahim Lawal','Engineering',  39 , 4),
    ('Fisayo Kolawole','Commercial',27, 5),
    ('Emmanuel Quartey','Growth',31,1),
    ('Awatt Bassey','Growth',32,2),
    ('Bolaji Akande','Revenue',30,3),
    ('Mohini Ufeli','Growth',29,1),
    ('King Makanjuola','Product',31,4),
    ('Ijeoma Opara','Revenue',26,2),
    ('Dipo Omobomi','Product',32,5),
    ('Dapo Awobokun','Revenue',35,3),
    ('Charles Idem','Revenue',38,1),
    ('Ayobami Alo','Product',34,4),
    ('Aminat Badara','Growth',30,2)''')

conn.commit()


cursor.execute('''SELECT name FROM TeamMembers WHERE division = 'Revenue' ''')
print("Team Members in Revenue Division:")
for row in cursor.fetchall():
    print(row[0])

cursor.execute('''SELECT name FROM TeamMembers WHERE division IN ('Growth', 'Product') AND age > 30 AND age < 35 ''')
print("\nTeam Members in Growth and Product Division whose age is greater than 30 years but less than 35 years:")
for row in cursor.fetchall():
    print(row[0])

cursor.execute('''SELECT name FROM TeamMembers WHERE module IN (1, 3, 5) ''')
print("\nTeam Members in Modules 1, 3, and 5:")
for row in cursor.fetchall():
    print(row[0])

cursor.execute('''SELECT name FROM TeamMembers WHERE module = 4 OR division = 'Product' ''')
print("\nTeam Members in Module 4 or Product Division:")
for row in cursor.fetchall():
    print(row[0])


conn.close()
