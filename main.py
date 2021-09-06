import datetime
import time
import requests
from plyer import notification

covidData = None
try:
    covidData= requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    print("Error!")

if(covidData!= None):
    data = covidData.json()["Success"]
    while(True):
        notification.notify(
            title= "Covid19 Stats on {}".format(datetime.date.today()),
            message = "Total Cases: {totalcases}\nToday's Cases: {todaycases}\nToday Deaths: {todaydeaths}\nTotal Active: {active}".format(
                totalcases=data['cases'],
                todaycases=data['todayCases'],
                todaydeaths=data["todayDeaths"],
                active=data['active']),
            app_icon="icon.ico",
            timeout=50
            )
        time.sleep(60*60*24*7)