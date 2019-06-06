from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import pyodbc

app = FlaskAPI(__name__)



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

    @app.route('/add_row', methods=['GET', 'POST'])

    def add_row(self):
        type = request.form("Type")
        title = request.form("Title")
        original_title = request.form("Original Title")
        is_adult = request.form("Adult Rating?")
        year = request.form("Year")
        endyear = request.form("End Year")
        runtime = request.form("Runtime")
        genre = request.form("Genre")

        self.query(f"INSERT INTO film_list ([type], title, original_title, is_adult, [year], endyear, "
                             f"runtime, genre)"
                             f"VALUES ('{type}', '{title}', '{original_title}', {is_adult},"
                             f"{year}, {endyear}, {runtime}, '{genre}')")

        self.docker_con.commit()

        return "Done!"

    @app.route('/add_row', methods=['GET', 'POST'])
    def addition(self):
        self.add_row()
        return render_template('form.html')