from pathlib import Path
from zipfile import ZipFile
import json

# with ZipFile("Files.zip", "w") as zip:
#     for p in Path("my folder").rglob("*.*"):
#         zip.write(p)

# with ZipFile("Files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("my folder/ali.txt")
#     print(info.file_size)
#     zip.extractall("extract")
# p = pathlib.Path(__file__)
# print(p)

# Working with json file
# movies = [
#     {"id": 1, "title": "Gajni", "year": 2009},
#     {"id": 2, "title": "3 idotes", "year": 2010},
# ]

# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)
