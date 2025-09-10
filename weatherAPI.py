from dotenv import load_dotenv
from os import getenv
import requests
from jsonpath_ng import jsonpath, parse

# loeading env file 
load_dotenv(dotenv_path='.env')

# getting the API key
WEATHER_API_KEY = getenv("WEATHER_API_KEY")

# list of all the indexs
indexs = {50:'good',100:'moderate',150:'unhealthy for sensitive group',200:'unhealthy',300:'very unhealthy',9999:'hazard'}

def getIndex(value:int) -> str:
    for index in indexs.keys():
        if value < index:
            return indexs[index]

def getAqi(city:str) -> str:
    # request the API with our TOKEN and the city
    r = requests.get(f"http://api.waqi.info/feed/{city}/?token={WEATHER_API_KEY}")

    if r.status_code != 200:
        return -1,"internal error"

    jsonData = r.json() # convert to JSON
    result = jsonData['data']['aqi'] # get the AQI value
    index = getIndex(result) # get the index

    return result,index

# example : getAqi('shangai')

