import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456", port=5432)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS person')

cur.execute(""" CREATE TABLE IF NOT EXISTS person(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
);
""")


cur.execute(""" INSERT INTO person (id, name, age, gender) VALUES
(1, 'Zhaka', 18, 'm'),
(2, 'Aka',   25, 'f'),
(3, 'China', 58, 'f'),
(4, 'Ayan',  34, 'f'),
(5, 'Miras', 10, 'm'),
(6, 'Aya',  34, 'm');
            
""")

cur.execute("""SELECT * FROM person WHERE name = 'Aka'; """)
print(cur.fetchone())

cur.execute("""SELECT * FROM person WHERE age < 50;""")
for row in cur.fetchall():
    print(row)

sql = cur.mogrify("""SELECT * FROM person WHERE starts_with(name, %s) AND age < %s;""", ("A", 30))   # похож на форматирование строк
print(sql)

conn.commit()

cur.close()
conn.close()

