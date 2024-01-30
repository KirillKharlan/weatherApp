import customtkinter as ctk
import os
import sqlite3
import modules.data.values as d_values
import threading
import modules.api as m_api
cities = ["Dnipro", "Kyiv", "Rome", "London", "Warsaw", "Prague"]
cities_Ua = ["Дніпро","Київ","Рим","Лондон","Варшава","Прага"]
#print(os.path.abspath(__file__+"/../../../data_base/data.db"),'\n',__file__)
try:
    data = sqlite3.connect(os.path.abspath(__file__+"/../../auto/data_base/data.db"))
except:
    try:
        data = sqlite3.connect(os.path.abspath(__file__+"/../../../auto/data_base/data.db"))
    except:
        data = sqlite3.connect(os.path.abspath(__file__+"/../../data_base/data.db"))
cursor = data.cursor()
full_name = d_values.get_value("Users",cursor,"name")[0][0]+" "+d_values.get_value("Users",cursor,"surname")[0][0]
try:
    city = d_values.get_value("Users",cursor,"place")[0][0]
except:
    city= "Дніпро"
status = "reg"
screen = ctk.CTk()
height = 0
width = 0
reg = False
path = os.path.abspath(__file__+"/../../fonts/RobotoSlap-bold.ttf")
list_api=[]
dict_api={"Dnipro":None,"Kyiv":None, "Rome":None, "London":None, "Warsaw":None, "Prague":None}
def data_api():
    global dict_api,list_api
    count=1
    for city in dict_api:
        print(city)
        api=m_api.get_api(city)
        dict_api[city]=api
        list_api += [api]
# data_api()
threading.Thread(target=data_api).start()
# list_api += [1]
print(list_api)
# Kyiv