import sqlalchemy
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pymysql
import mysql
from urllib.request import urlopen
from sqlalchemy import create_engine

url="https://www.scrapethissite.com/pages/forms/"
query=""
page=requests.get(url+query)
print(page.status_code)
soup=BeautifulSoup(page.content, "html.parser")
#print(soup.find("table"))
#print(soup.findAll("th"))
# for i in soup.findAll("th"):
#     print(i.get_text().strip())
#     #print(i.text.strip())
#

header = [i.text.strip() for i in soup.find_all("th")]
df=pd.DataFrame(columns=header)
# print(df)
# print(len(df.columns))
column=soup.find_all("tr")
for row in column[1:]:
    row_data=row.find_all("td")
    data = [i.text.strip() for i in row_data]
    df.loc[len(df)] = data
print(df)
#df.to_csv("./hockeyteam.csv")
password = r"Jovan@2023"
engine=sqlalchemy.create_engine('mysql+mysqldb://root:{password}@localhost:3306/mydb1', echo = False)
df.to_sql('hockey_team', engine, if_exists='replace', index=False)
