from gc import freeze

import mysql.connector
import  os




class DB:
    def __init__(self):
        password = os.getenv("DB_Password")
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=password,
                port=3306,
                database="airline"

            )

            self.mycursor=self.conn.cursor()
            print("Conncection Establised")

        except:
            print('Conection Error')


    def fetch_city_names(self):
        self.mycursor.execute("""
        SELECT distinct(source_city) FROM airline.aeroplane_detail;
        """)

        data=self.mycursor.fetchall()

        return  data

    def flight_detail(self,source,destination,departure_time,arrival_time,airline):
        query="""
        select * from aeroplane_detail
        where source_city= %s and destination_city=%s and departure_time=%s and arrival_time=%s and airline=%s;
        """

        self.mycursor.execute(query,(source,destination,departure_time,arrival_time,airline))
        data=self.mycursor.fetchall()
        return data


    def fetch_airline_freq(self):
        airline=[]
        frequency=[]
        self.mycursor.execute("""
        select airline,count(*) as "frequency" from
aeroplane_detail group by airline;
        """)

        data=self.mycursor.fetchall()

        for i in data:
            airline.append(i[0])
            frequency.append(i[1])

        return  airline,frequency


    def fetch_avg_price(self):
        self.mycursor.execute("""
        select airline ,avg(price) as "Avg_price" from
airline.aeroplane_detail
group by airline;""")

        data=self.mycursor.fetchall()

        avg_price=[]
        airline=[]

        for i in data:
            avg_price.append(i[1])
            airline.append(i[0])

        return airline,avg_price




    def departure_time(self):

        self.mycursor.execute(""" 
         select distinct(departure_time) from
aeroplane_detail;""")

        data=self.mycursor.fetchall()

        return data

    def arrival_time(self):

        self.mycursor.execute(""" 
             select distinct(arrival_time) from
    aeroplane_detail;""")

        data = self.mycursor.fetchall()

        return data


    def fetch_airline(self):

        self.mycursor.execute(""" 
        select distinct(airline) from aeroplane_detail""")

        data=self.mycursor.fetchall()

        return data

  









