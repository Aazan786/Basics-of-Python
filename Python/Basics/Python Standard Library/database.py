import mysql.connector
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())

connection = mysql.connector.connect(
    host="localhost", user="root", password="root", database="movies"
)

cursor = connection.cursor()

query = "INSERT INTO movies VALUES(?,?,?)"
for movie in movies:
    cursor.execute(query, tuple(movie.values()))
cursor.commit()

# rows = cursor.fetchall()
# for i in rows:
#     print(i)
