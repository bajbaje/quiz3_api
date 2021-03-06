import requests
import json

url = "https://pixabay.com/api/"
key = "27211759-a2723440d6ac6b96bc4fdfe90"
search = input('what kind of images would you like to see: ') # lets us use search words for example: sky+flowers
amount = 3
payload = {'key': key, 'q': search, 'per_page': amount}
response = requests.get(url, params=payload)

# 1. using requests module functions

print(response.status_code)
print(response.content)
print(response.headers)

res = response.json()

pic1 = requests.get(res['hits'][0]["largeImageURL"])
pic2 = requests.get(res['hits'][1]["largeImageURL"])
pic3 = requests.get(res['hits'][2]["largeImageURL"])


file = open('pic1.jpg', 'wb')
file.write(pic1.content)

file = open('pic2.jpg', 'wb')
file.write(pic2.content)

file = open('pic3.jpg', 'wb')
file.write(pic3.content)

# 2. adding information into json file

with open("data.json", "w") as file:
    json.dump(res, file, indent=4)

# 3. using json/dict functions

id = json.dumps(res['hits'][0]["id"])
views = json.dumps(res['hits'][0]["views"])
downloads = json.dumps(res['hits'][0]["downloads"])
likes = json.dumps(res['hits'][0]["likes"])

print(f'First image id is: {id}, It has {views} views, {downloads} downloads and {likes} likes.')

# 4. creating and adding information into a table

import sqlite3

conn = sqlite3.connect('pictures.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE information
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_id INTEGER,
            views INTEGER ,
            downloads INTEGER ,
            likes INTEGER);''')


cursor.execute("INSERT INTO information (image_id, views, downloads, likes) VALUES(?, ?, ?, ?)",
               (id, views, downloads, likes))
conn.commit()


conn.close()




