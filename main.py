import requests
from bs4 import BeautifulSoup
import pandas as pd

url1 = "https://weather.com/en-IN/weather/tenday/l/62fbad342762884be6174b55022774f2c11c03a2c8c27ff177a0a8a47b932548"

page = requests.get(url1)
soup = BeautifulSoup(page.content, "html.parser")
'''indexAll = "detailIndex"
summary = []

for i in range(7):
    indexAll = indexAll + str(i)
    x = soup.find(id = indexAll)
    indexAll = "detailIndex"
    a = x.find_all(class_ = "DailyContent--narrative--3AcXd")
    Con = "At night,".join([p.text for p in a])
    summary.append(Con)
#print(summary)'''
Title = soup.find(class_ = "LocationPageTitle--PresentationName--Injxu").getText()
print(f"Current Location: {Title}")

indexAll = "titleIndex"
days = []
for i in range(7):
    indexAll = indexAll + str(i)
    a = soup.find(id = indexAll)
    days.append(a)
    indexAll = "titleIndex"
dayNames = []
tempHigh = []
tempLow = []
short_desc = []
for i in range(7):
    dayName = days[i].find(class_ = "DetailsSummary--daypartName--1Mebr").getText()
    tempH = days[i].find(class_ = "DetailsSummary--highTempValue--3x6cL").getText()
    tempL = days[i].find(class_ = "DetailsSummary--lowTempValue--1DlJK").getText()
    desc = days[i].find(class_ = "DetailsSummary--extendedData--aaFeV").getText()
    dayNames.append(dayName)
    tempHigh.append(tempH)
    tempLow.append(tempL)
    short_desc.append(desc)

weather_table = pd.DataFrame({
    "Date":dayNames,
    "Max Temperature":tempHigh,
    "Min Temperature":tempLow,
    "Short Description":short_desc
})

print(weather_table)
weather_table.to_csv("weather.csv")
