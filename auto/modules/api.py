import requests
import modules.data_base as m_data
import time
import os 
# import json
import io
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
def image_2(data,day,hour):
    # try:
        icon=str(data["forecast"]["forecastday"][int(day)]["hour"][hour]["condition"]["icon"])
        count=icon.split("/")[-1].split(".")[0]
        time_3=icon.split("/")[-2]
        print(count,time_3,-142)
        day_dict = {
            "113":'sun_2412787',
            "116":"sunny_2412794",
            "119":"sunny_2412798",
            "122":"sunny_2412798",
            "143":"sunny_2412798",
            "176":"rainy_2412747",
            "179":"snowy_2412767",
            "182":"snowy_2412768",
            "182":"snowy_2412768",
            "185":"snowy_2412766",
            "200":"storm_2412772",
            "227":"snowy_2412766",
            "230":"snowy_2412766",
            "248":"drizzle_2412691",
            "260":"drizzle_2412691",
            "263":"rainy_2412747",
            "266":"rainy_2412747",
            "281":"snowy_2412766",
            "284":"snowy_2412766",
            "293":"rainy_2412747",
            "296":"rainy_2412747",
            "299":"rainy_2412747",
            "302":"rainy_2412747",
            "305":"rainy_2412747",
            "308":"rainy_2412747",
            "311":"drizzle_2412695",
            "314":"drizzle_2412695",
            "317":"drizzle_2412695",
            "320":"drizzle_2412695",
            "323":"snowy_2412768",
            "326":"snowy_2412768",
            "329":"snowy_2412768",
            "332":"snowy_2412768",
            "335":"snowy_2412768",
            "338":"snowy_2412768",
            "350":"snowy_2412768",
            "353":"rainy_2412747",
            "356":"rainy_2412747",
            "359":"rainy_2412747",
            "362":"rainy_2412747",
            "365":"snowy_2412768",
            "368":"snowy_2412768",
            "371":"snowy_2412768",
            "374":"snowy_2412768",
            "377":"snowy_2412768",
            "386":"storm_2412772",
            "389":"storm_2412772",
            "392":"storm_2412772",
            "395":"storm_2412772",
        }
        # snowy_2412768
        # snowy_2412767
        night_dict = {
            "113":'moon_2412729',
            "116":"moon_2412729",
            "119":"moon_2412729",
            "122":"moon_2412729",
            "143":"moon_2412729",
            "176":"rain_2412733",
            "179":"snowy_2412767",
            "182":"snowy_2412767",
            "182":"snowy_2412767",
            "185":"snowy_2412766",
            "200":"storm_2412772",
            "227":"snowy_2412766",
            "230":"snowy_2412766",
            "248":"drizzle_2412691",
            "260":"drizzle_2412691",
            "263":"rain_2412733",
            "266":"rain_2412733",
            "281":"snowy_2412766",
            "284":"snowy_2412766",
            "293":"rain_2412733",
            "296":"rain_2412733",
            "299":"rain_2412733",
            "302":"rain_2412733",
            "305":"rain_2412733",
            "308":"rain_2412733",
            "311":"drizzle_2412691",
            "314":"drizzle_2412691",
            "317":"drizzle_2412691",
            "320":"drizzle_2412691",
            "323":"snowy_2412767",
            "326":"snowy_2412767",
            "329":"snowy_2412767",
            "332":"snowy_2412767",
            "335":"snowy_2412767",
            "338":"snowy_2412767",
            "350":"snowy_2412767",
            "353":"rain_2412733",
            "356":"rain_2412733",
            "359":"rain_2412733",
            "362":"rain_2412733",
            "365":"snowy_2412767",
            "368":"snowy_2412767",
            "371":"snowy_2412767",
            "374":"snowy_2412767",
            "377":"snowy_2412767",
            "386":"storm_2412772",
            "389":"storm_2412772",
            "392":"storm_2412772",
            "395":"storm_2412772",
        }
        path= os.path.abspath(__file__+"/../../images/")
        if time_3 == "day":
            return os.path.abspath(__file__+"/../../images/"+day_dict[count] + ".png")
        elif time_3 == "night":
            return os.path.abspath(__file__+"/../../images/"+night_dict[count] + ".png")
        # else:
            # return io.BytesIO(requests.get("https:"+ icon).content)
        return io.BytesIO(requests.get("https:"+ icon).content)
    # except:
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
def time_2(hour:str="8:00 PM"):
    hour = str(hour).split(" ")
    if hour[1]== "PM":
        hour[0] =f"{int(hour[0].split(':')[0])+12}:{hour[0].split(':')[1]}"
    return hour[0].split(":")
# 71e3b6535e7a4a359b2124944242401
# http://api.weatherapi.com/v1/forecast.json?key={key_API}&q={city}&days=2&aqi=no&alerts=no
def get_api_2(city_name=None):
    if city_name == None:
        city_name = m_data.city
    url_api=f"http://api.weatherapi.com/v1/forecast.json?key=71e3b6535e7a4a359b2124944242401&q={city_name}&days=2&aqi=no&alerts=no"
    response=requests.get(url = url_api)
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