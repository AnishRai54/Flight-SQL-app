import pandas as pd
# import os
#
# import mysql.connector
# password=os.getenv("DB_Password")
# try:
#     conn = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password=password,
#         port=3306,
#
#     )
#
#     mycursor=conn.cursor()
#     print("Conncection Establised")
#
# except:
#     print('Conection Error')


# mycursor.execute("create database Airline")
# conn.commit()

# import pandas as pd
#
# df=pd.read_csv("airlines_flights_data.csv")
#
# from sqlalchemy import create_engine
#
# # engine = create_engine(
# #     "mysql+pymysql://root:{}@localhost:3306/Airline".format(password)
# # )
# #
# # df.to_sql(
# #     name="aeroplane_detail",
# #     con=engine,
# #     if_exists="replace",   # or "append"
# #     index=False
# # )
# #
# # print("✅ Table imported")



import streamlit as st
from sqlalchemy import values
from tenacity import retry

from dbhelper import DB
import plotly.express as px

import plotly as plt




db=DB()


st.sidebar.title("Flight Analytics")


user_option=st.sidebar.selectbox("Menu",['Select One','Check Flights','Analytics'])

if user_option=="Select One":



    st.title("Flight Performance Analytics")
    st.text("""✈️ Flight Analytics Dashboard is an interactive data analytics application designed to provide a clear and concise overview of airline operations and flight performance. The dashboard transforms structured flight data into actionable insights by analyzing total flights, active airlines, source–destination routes, city-wise traffic distribution, and on-time versus delayed flights. Built using SQL, Python, Plotly, and Streamlit, it enables users to quickly identify busiest routes, compare airline performance, and understand operational trends through interactive visualizations, supporting data-driven decision-making from a single, easy-to-understand page.""")

if user_option=="Check Flights":
    st.title("Check Flights")

    col1,col2=st.columns(2)

    with col1:
        data=[i[0] for i in db.fetch_city_names()]

        source=st.selectbox("Source",data)

    with col2:
        data = [i[0] for i in db.fetch_city_names()]
        destination=st.selectbox("Destination", data)

    col3,col4=st.columns(2)

    with col3:
        departure_time_list=db.departure_time()
        departure_time=[i[0] for i in departure_time_list]

        select_1=st.selectbox("Departure Time",departure_time)





    with col4:
        arrival_time_list = db.arrival_time()
        arrival_time = [i[0] for i in arrival_time_list]

        select_2=st.selectbox("Arrival Time", arrival_time)



    airline_list_1=db.fetch_airline()
    airline_list=[i[0] for i in airline_list_1]

    airline=st.selectbox("Select airline",airline_list)




    if st.button("Search"):
        result=db.flight_detail(source,destination,select_1,select_2,airline)
        st.dataframe(result)


elif user_option=="Analytics":
    airline,frequency=db.fetch_airline_freq()

    data={
        "airline": airline,
        "frequency":frequency
    }

    df=pd.DataFrame(data)

    fig=px.pie(
        df,names="airline",values="frequency")
    st.title("Frequency Of Airline")
    st.plotly_chart(fig,use_container_width=True)


    airline_1,avg_price=db.fetch_avg_price()

    data_1={
        "airline":airline_1,
        "avg_price":avg_price
    }
    df_1=pd.DataFrame(data_1)



    fig=px.bar(df_1,x="airline",y="avg_price")

    st.title("Average Price of Airline")

    st.plotly_chart(fig,use_container_width=True)




