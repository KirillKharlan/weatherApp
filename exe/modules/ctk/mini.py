import modules.data_base as m_data
import modules.data.values as d_values
#import modules.ctk.start as c_start 
# ↑↓ 1⁰=
import modules.api as m_api
import modules.ctk.text as ct_text
import modules.ctk.big_screen as ct_big
from PIL import Image
import customtkinter as ctk
import os
import threading
import time
big_screen_1 = False
count = 0
def set_value():
    global count 
    time.sleep(1)
    count = 0
def big_screen():
    global count
    count += 1 
    if  count  == 2:
        global big_screen_1
        big_screen_1 = True
        ct_big.create()
    threading.Thread(target=set_value).start()
    # set_value()
screen = m_data.screen
screen.iconbitmap(os.path.abspath(__file__+"/../../../icon.ico"))
screen.resizable(0,0)
screen.title("mini screen")
m_data.width = 350
m_data.height  = 350
screen.geometry(f"{m_data.width}x{m_data.height}+{50}+{50}")
def mini_screen(seconds = 0):
    global big_screen_1
    print(seconds)
    time.sleep(seconds)
    if not big_screen_1:
        data = m_api.get_api()
        print(data)
        screen = m_data.screen
       
        background = ctk.CTkButton(master=screen,width=m_data.width,height=m_data.height,text="",border_width=5,fg_color="#5DA7B1",border_color="#096C82",hover= False,corner_radius=20,command=big_screen)
        background.place(x = 0,y = 0)
        img1 = Image.open(os.path.abspath(__file__+"/../../../images/captcha_6741193.png"))
        img2 = Image.open(os.path.abspath(__file__+f"/../../../images/{m_api.image(data)}.png"))
        img6 = ctk.CTkImage(dark_image=img1,size=(25,25))
        img5 = ctk.CTkImage(dark_image=img2,size=(179.59,142))
        img3 = ctk.CTkLabel(master=screen,image=img5,width=15,text="",fg_color="#5DA7B1")
        img4 = ctk.CTkLabel(master=screen,image=img6,width=15,text="",fg_color="#5DA7B1")
        img4.place(x=300,y=20)
        img3.place(x=17,y=18)
        font = ctk.CTkFont(family=m_data.path,size=40,weight=("bold"))
        city = None
        text1 = ctk.CTkLabel(font=font,master=screen,width=1,height=52,text=data["name"],text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
        for count in range(6):
            print(m_data.cities[count])
            if data["name"] == m_data.cities[count]:
                
                text1 = ctk.CTkLabel(font=font,master=screen,width=1,height=52,text=m_data.cities_Ua[count],text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
        text1.place(x = 180,y = 274)
        temp = m_api.temp(data["main"]["temp"])
        min_temp = m_api.temp(data["main"]["temp_min"])
        max_temp =  m_api.temp(data["main"]["temp_max"])
        
        temp_x = 290 - len(temp)*31
        text7 = ct_text.Text(text=f"{temp}⁰",x=temp_x,y=199,height=71,width=61,size=80,master= screen)
        if len(min_temp)<3:
            text8 = ct_text.Text(text=f"↑{max_temp}⁰",x=118,y=223,height=30,width=55.06,size=30,master=screen)
        else:
            text8 = ct_text.Text(text=f"↑{max_temp}⁰",x=140,y=223,height=30,width=55.06,size=30,master=screen)
        text9 = ct_text.Text(text=f"↓{min_temp}⁰",x=57,y=223,height=30,width=46.21,size=30,master=screen)
        text11 = ct_text.Text(text="з проясненнями ",x=47,y=188.5,height=26.5,width=0,size=21,master=screen)
        text10 = ct_text.Text(text="Хмарно",x=47,y=162,height=1,width=0,size=30,master=screen)
        #  ct_text.Text(text="↑11⁰",x=188.94,y=223,height=30,width=55.06,size=30)
        # text9
        threading.Thread(target=mini_screen,args=[120],daemon=True).start()
    
mini_screen()
m_data.screen.mainloop()