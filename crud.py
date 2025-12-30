import os

import mysql.connector
password=os.getenv("DB_Password")
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password=password,
        port=3306,
        database='flight'
    )

    mycursor=conn.cursor()
    print("Conncection Establised")

except:
    print('Conection Error')


# Create a Database using python

mycursor.execute("select * from airline ")
data=mycursor.fetchall()
print(data)

print()
for i in data:
    print(i[3])

# update
mycursor.execute("""
update airline set name="Chhatrapati Shivaji Maharaj International Airport"
where airport_id=2
""")
conn.commit()



# DElete

mycursor.execute("delete from airline where airport_id=2")
conn.commit()

mycursor.execute("select * from airline ")
data=mycursor.fetchall()
print(data)

