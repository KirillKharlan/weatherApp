import requests
import modules.data_base as m_data
import time
# import json
api_key = "6e8d75051d7d7e2e2687d40ab7a5f132"

def temp(kelvin:float):
    return str(int(kelvin-273.15))
def image(data): 
    name = None
    weather = data["weather"][0]["icon"]
    main = data["weather"][0]["main"]
    # print("n" in weather)
    if weather == "01d":
        name = "sun_2412787"

    elif weather == "02d":
        name = "sunny_2412794"
        
    elif weather == "02n":
        name = "moon_2412729"

    elif weather == "03d" or weather== "04d":
        name = "sunny_2412798"

    elif weather == "09d":
        name ="rainy_2412747"

    elif weather == "09n":
        name = "rain_2412733"

    elif weather == "10n":
        name = "drizzle_2412691"

    elif weather == "10d":
        name = "drizzle_2412695"

    elif weather == "11n" or weather == "11d":
        name = "storm_2412772"

    elif weather == "13d":
        name = "snowy_2412768"   

    elif weather == "13n":
        name = "snowy_2412767"
    # Snow Clouds Clear Mist Rain
    elif main == "Snow":
        if "n" in weather:
            name ="snowy_2412767"
        elif "d" in weather:
            name = "snowy_2412766"
    elif main == "Clouds":
        if "n" in weather:
            name ="moon_2412729"
        elif "d" in weather:
            name = "sunny_2412798"
    elif main == "Clear":
        if "n" in weather:
            name ="moon_2412729"
        elif "d" in weather:
            name = "sun_2412787"
    elif main == "Rain":
        if "n" in weather:
            name ="rain_2412733"
        elif "d" in weather:
            name = "rainy_2412747"
    elif main == "Mist":
        if "d" in weather:
            name  = "drizzle_2412695"
        elif "n" in weather:
            name = "drizzle_2412691"
    else:
        name = "snowy_2412766"
    return name
    #if name == "snow"
def time1(data:dict,sun = "set"):
    time3 = time.localtime()
    time2 = data["sys"]["sun"+sun]
    year = int(time2/60/60/24//365+1970)
    #year2 = time2/60/60/24/365 -int(time2/60/60/24//365)
    sec = time2%60
    minute = int((time2-sec)%3600/60)
    hour = int(((time2-sec-minute*60)%216000/60/60-3+time3[3])%24)
    day =  int(((time2-sec-minute*60)%216000/60/60-3+time3[3])/24)
    #print(time2,sec,minute,hour,year)
    if len(str(minute))==1:
        minute=str(0)+str(minute)
    if len(str(hour))==1:
        hour=str(0)+str(hour)
    if sun == "set":
        sun = "Захід"
    else:
        sun = "Схід"
    return {
        "minute": str(minute),
        "hour": str(hour),
        "year": str(year)[-2]+str(year)[-1],
        "day": day,
        "text": str(sun)+str(" сонця о ")+str(hour)+":"+str(minute)
    }
    # Захід сонця о 20:2
def text(data):
    name = data["weather"][0]["main"]
    text = ""
    if name == "Snow":
        text = "Засніжено"
    elif name == "Rain":
        text = "Дощливо"
    elif name == "Clear":
        text = "Ясно"
    elif name == "Clouds":
        text = "Хмарно"
    elif name == "Mist":
        text = "Тумано"
    else:
        text = "Хмарно"
    return text
def get_api(city_name = None,add=""):
    if city_name == None:
        city_name = m_data.city
    url_api = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"+add
    response = requests.get(url = url_api)
    if response.status_code == 200:
        data = response.json()
        #time1(data)
        #print (time1(data))
        # time1(data,"rise")
        return data
    else:
        print("Error response",city_name)
        print(response)
        return response.status_code
