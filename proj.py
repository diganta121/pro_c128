from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

# URL
URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver

page = requests.get(URL)

time.sleep(10)

data = []


def scrape():
    time.sleep(2)

    soup = BeautifulSoup(page.text, "html.parser")

    table1 = soup.find_all("table", {"class": "wikitable sortable"})

    trs = table1[0].find_all("tr")

    for tr in trs:
        tds = tr.find_all("td")

        temp_list = []
        for td in tds:
            try:
                cont = td.text.rstrip()
                temp_list.append(cont)
            except:
                temp_list.append("")
            data.append(temp_list)

    final_csv = []
    for i in data:
        final_csv.append([i[0], i[5], i[8], i[9]])
    print(final_csv)

    headers = ["Star_name", "Distance", "Mass", "Radius"]
    df2 = pd.DataFrame(
        list(final_csv),
        columns=["Star_name", "Distance", "Mass", "Radius"],
    )
    df2.to_csv("dwarf_stars.csv", index=True, index_label="id")


# f = open("proj_csv.csv", "w", newline="")
# wr = csv.writer(f)
# for i in range(len(final_csv)):
#     wr.writerow(final_csv[i])
# f.close()


scrape()
print(data)
