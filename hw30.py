import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS table1 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')

data_table1 = [
    ('Avtandil Javrishvili', 17),
    ('Nini Jabanashvili', 18),
    ('Giorgi Pataridze', 16),
    ('Elza ositashvili', 47),
    ('Nika Cicqishvili', 25)
]

cursor.executemany('INSERT INTO table1 (name, age) VALUES (?, ?)', data_table1)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS table2 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        price REAL
    )
''')

data_table2 = [
    ('Laptop', 1200.50),
    ('Smartphone', 699.99),
    ('Headphones', 89.99),
    ('Camera', 549.95),
    ('Tablet', 399.99)
]

cursor.executemany('INSERT INTO table2 (product, price) VALUES (?, ?)', data_table2)

conn.commit()
conn.close()
