from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
import pandas as pd

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Edge("/Users/aarif/Desktop/c127_Rithika/msedgedriver.exe")
browser.get(start_url)

time.sleep(2)

planets_data = []

def scrape():
    for i in range(0,100):
        print("Scraping of page - is done ",i+1)

        soup = BeautifulSoup(browser.page_source,"html.parser")

        for ul_tag in soup.find_all("ul",attrs={"class":"exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list =[]

            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planets_data.append(temp_list)
        browser.find_element(by = By.XPATH,value = '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    print(planets_data[1])


scrape()
# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planetdf = pd.DataFrame(planets_data , columns = headers)

# Convert to CSV
planetdf.to_csv("Scrapeddata.csv", index = True , index_label = "id")