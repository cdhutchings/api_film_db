import pyodbc

class SqlConn:

    def __init__(self, server="localhost,1433", database="movies", username="SA", password="Passw0rd2018"):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.docker_con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL '
                                'Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        self.cursor = self.docker_con.cursor()

    def query(self, sql_query):

        return self.cursor.execute(sql_query)

