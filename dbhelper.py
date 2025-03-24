import mysql.connector
import pandas as pd

class DB:
    def __init__(self):
        # connect to database
        try:
            self.conn = mysql.connector.connect(host='localhost',user='root',password='jarvis',database='flight')
            self.mycursor = self.conn.cursor()
            print('Connection established')

        except:
            print('Connection error')

    def fetch_cities(self):
        city_list = []
        self.mycursor.execute("""
            SELECT Source FROM flight.flight
            UNION
            SELECT Destination FROM flight.flight;
        """)
        cities = self.mycursor.fetchall()
        for city in cities:
            city_list.append(city[0])
        return city_list

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
            SELECT Airline,Route,Dep_Time,Duration,Price FROM flight.flight
            WHERE Source = '{}' AND Destination = '{}'
        """.format(source,destination))

        data = self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline = []
        freq = []
        self.mycursor.execute("SELECT Airline,COUNT(*) FROM flight.flight GROUP BY Airline")
        data = self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            freq.append(item[1])

        return airline,freq

    def busy_airport(self):
        city = []
        freq = []
        self.mycursor.execute("""SELECT Source,COUNT(*) FROM (SELECT Source FROM flight.flight
                                UNION ALL
                                SELECT Destination FROM flight.flight) t
                                GROUP BY t.Source
                                ORDER BY COUNT(*) DESC""")

        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            freq.append(item[1])
            df = pd.DataFrame({'city':city,'frequency':freq})
        return df

    def daily_frequency(self):
        date = []
        frequency1 = []
        self.mycursor.execute("""SELECT Date_of_Journey,COUNT(*) FROM flight
                                GROUP BY Date_of_Journey
        """)
        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency1.append(item[1])

        df1 = pd.DataFrame({'date':date,'frequency':frequency1})
        return df1
