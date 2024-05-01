import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456", port=5432)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS phonebook')

cur.execute(""" CREATE TABLE IF NOT EXISTS phonebook(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            surname VARCHAR(255),
            phonenumber VARCHAR(11)
);
""")

cur.execute(""" INSERT INTO phonebook (id, name, surname, phonenumber) VALUES
(1, 'Zhaksylyk', 'Zhaka', 87757770000),
(2, 'Akbar', 'Aka',    87769871300),
(3, 'Shyngys', 'China',   87077465360),
(4, 'Alex', 'Ale',      87784886806),
(5, 'Ivan', 'Ivanushka',  87780441865),
(6, 'Ayan', 'Ayanchik' , 87475895015),
(7, 'Miras', 'Mayra', 87470122354),
(8, 'Marat', 'Mara', 87750054994),
(9, 'Max', 'Maxi',  87057428066),
(10,'Akhat', 'Akho', 87017481646);
""")


# update data
cur.execute('''UPDATE phonebook 
            SET name = 'China', phonenumber = 87014567891
            WHERE id = 3;
            ''')


# special query for who's name starts with "A" or who has tele2 operator
cur.execute("""SELECT id, name,surname, phonenumber FROM phonebook WHERE SUBSTR(name,1,1) = 'A' """)
for row in cur.fetchall():
    print(row)

print('\n')

cur.execute("""SELECT id, name,surname, phonenumber FROM phonebook WHERE SUBSTR(phonenumber,1,4) = '8747' """)
for row in cur.fetchall():
    print(row)


# delete datas who's name is "Akhat" or who has altel operator
print('\n')
cur.execute("""DELETE FROM phonebook WHERE name = 'Akhat' OR SUBSTR(phonenumber,1,4) = '8705' """)
cur.execute('SELECT * FROM phonebook')
for row in cur.fetchall():
    print(row)


conn.commit()
cur.close()
conn.close()