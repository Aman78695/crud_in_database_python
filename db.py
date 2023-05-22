import mysql.connector
class dbhelper:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(
                host='localhost',
                user='root',
                password='aman',
                database='indigo')
            self.mycursor=self.conn.cursor()

        except mysql.connector.Error as error:
            print(error)
    def fetchcity(self):
        l=[]
        self.mycursor.execute('''select distinct(source) from flights
                                union
                                select distinct(destination) from flights''')
        data=self.mycursor.fetchall()
        for item in data:
            l.append(item[0])
        return l
    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""select airline,Date_of_Journey,Dep_time,price from flights
                            where source='{}' and destination='{}'""".format(source,destination))
        records=self.mycursor.fetchall()
        return records

    def flight_piechart(self):
        m=[]
        n=[]
        self.mycursor.execute("""select airline,count(*) from flights group by airline""")
        data=self.mycursor.fetchall()
        for item in data:
            m.append(item[0])
            n.append(item[1])
        return m,n
