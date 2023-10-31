# create file

# with open("Failas.txt", "w") as f:
#     content = f.write("hello world")

#Open file


# with open("Failas.txt", "r") as f:
#     content = f.read()
# print(content)


# with open("Failas.txt", "a") as f:
#     content = f.write("\ndar viena teksto eilute")
# print(content)

import requests
from bs4 import BeautifulSoup
import psycopg2

# 200 OK
# 301 - 302 - File found
# 403 Forbidden
# 404 - file not found
# 500 server error

flats_data = []
#
# def create_and_insert_flats ():
#
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="Aruodas",
#         user="postgres",
#         password="Samagonas123"
#     )
#
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS aruodas_uzsienis(
#             id SERIAL primary key,
#             flat_title VARCHAR(300),
#             flat_price DECIMAL(10,2)
#         )
#     """
#
#     cursor.execute(create_table_query)
#     print("Table created Succesfully!")
#
#
#     url = "https://www.aruodas.lt/uzsienio-objektai/"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     content_block = soup.select('div.project-list-content div')
#     #
#     # print(content_block)
#
#     for content in content_block:
#         try:
#             flat_title = content.find("div", class_="top-three-adverts__advert__address").text.strip()
#             flat_price = content.find("span", class_="top-three-adverts__advert__price__price").text.strip()\
#                 .replace("€", "").replace(" ", "").split(sep="_")[0]
#
#
#
#             # print(flat_title, flat_price)
#             # flats_data.append((flat_title, flat_price))
#             insert_query = "INSERT INTO aruodas_uzsienis (flat_title, flat_price) VALUES (%s, %s)"
#             cursor.execute(insert_query, (flat_title, flat_price))
#         except AttributeError:
#             continue
#     connection.commit()
#
# create_and_insert_flats()








flats_data = []
def create_and_insert_flats():
    #kuriam connectiona prie duomenu bezes:
    connection = psycopg2.connect(
        host = "localhost",
        port = 5432,
        database = "Aruodas",
        user="postgres",
        password = "Samagonas123"
    )

    cursor = connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS aruodas_uzsienis(
            id SERIAL primary key,
            flat_title VARCHAR(300),
            flat_price DECIMAL(10,2)
        )
    """

    cursor.execute(create_table_query)
    print("Table created Successfully!")


    url = "https://www.aruodas.lt/uzsienio-objektai/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    content_block = soup.select('div.project-list-item')

    for content in content_block:
        try:
            flat_title = content.find("h2", class_="project-title-full project-title").text.strip()
            flat_price = content.find("h3", class_="project-title-full project-min-values").text.strip() \
                .replace(" ", "").replace("€", "").split(sep="Kaina:")[1]
            cursor.execute("select 1 from aruodas_uzsienis where flat_title = %s and flat_price = %s",
            (flat_title, float(flat_price)))
            exists = cursor.fetchone()
            if not exists:
                cursor.execute("INSERT INTO aruodas_uzsienis (flat_title, flat_price) VALUES (%s, %s)",
            (flat_title, float(flat_price)))
            # print(flat_title, flat_price)
            # flats_data.append((flat_title, flat_price))



        except AttributeError:
            continue
    print("Flats inserted successfully!")


    connection.commit()

create_and_insert_flats()