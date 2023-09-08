import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/List_of_largest_banks_in_the_United_States"
page=requests.get(url)
print(page.status_code)# 20*# --check the website

#print(page.content)
soup = BeautifulSoup(page.content, "html.parser")
#print(soup.text)
# print(soup.find("p"))# first occurence
# print(soup.find_all("p")) # finds all tags
table = soup.find("table", class_="wikitable")
table_header = table.find_all("th")#---list
#print(table_header[0].text)
# for header in table_header:
#     print(header.text.strip())
head_list = [h.text.strip() for h in table_header]
print(head_list)
df=pd.DataFrame(columns=head_list)
print(df)
table_row_data = table.find_all("tr")
#print(table_row_data)
for row in table_row_data[1:]:
    #print(row.find_all("td"))#---list
    # for data in row.find_all("td"):
    #     print(data.text)
    row_list = [data.text.strip() for data in row.find_all("td")]
    print(row_list)
    print(len(df))
    df.loc[len(df)]=row_list

df.to_csv("./bank.csv")
df.to_excel("./largest_banks.xlsx")





