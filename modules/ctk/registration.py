import modules.data_base as m_data
import customtkinter as ctk 
import modules.api as m_api
import os 
import modules.data.values as d_value
import modules.ctk.start as ctk_start
m_data.screen.title("регістрація користувача")

m_data.width = 460
m_data.height = 645
m_data.screen.geometry(f"{m_data.width}x{m_data.height}+{m_data.screen.winfo_screenwidth()//2-m_data.width//2}+{m_data.screen.winfo_screenheight()//2-m_data.width//2}")
def registration():
    global button,name_entry,surname_entry,country_entry,place_entry
    #get бере текст який ми вказуємо у текстовому полі
    place = place_entry.get()
    api = m_api.get_api(place)
    #print(d_value.get_value(cursor=m_data.cursor,name_table="Users",name_column="place"))
    if type(api) == type(1):
        try:
            api = m_api.get_api(d_value.get_value(cursor=m_data.cursor,name_table="Users",name_column="place")[0][0])
        except:
            pass
    #print(api)
    if type(api) != type(1):

        for city in m_data.cities:
            if api["name"]==city:
                m_data.city = city
                country = country_entry.get()
                name = name_entry.get()
                surname = surname_entry.get()
                enter  = False
                value = d_value.get_value(cursor=m_data.cursor,name_table="Users",name_column="reg")
                print(d_value.get_value(cursor=m_data.cursor,name_table="Users"))
                if surname != "" != place != "" != name != "" != country and (not value  or m_data.reg):
                    enter = True
                    m_data.cursor.execute("INSERT INTO Users (reg,name,surname,country,place) VALUES (?,?,?,?,?)",(1,name,surname,country,api["name"]))
                

                if enter or value:
                    m_data.reg=True
                    m_data.full_name = d_value.get_value("Users",m_data.cursor,"name")[0][0]+" "+d_value.get_value("Users",m_data.cursor,"surname")[0][0]
                    text1.destroy()
                    button.destroy()
                    name_entry.destroy()
                    surname_entry.destroy()
                    country_entry.destroy()
                    place_entry.destroy()
                    ctk_start.create()
def enter():
    global button,name_entry,surname_entry,country_entry,place_entry,text1 
    font = ctk.CTkFont(family=m_data.path,size=28,weight=("bold"))
    
    text1 = ctk.CTkLabel(font=font,master=m_data.screen,width=380,height=55,text="Реєстрація користувача",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text1.place(x = 38,y = 42)

    button = ctk.CTkButton(font= font,master=m_data.screen,width=218,height=46,text="Зберегти",border_width=3,fg_color="#096C82",command=registration, border_color= "#FFFFFF",text_color="#FFFFFF",corner_radius=20,bg_color="#5DA7B1")
    button.place(x = 119,y = 546)

    name_entry = ctk.CTkEntry(font=font,master=m_data.screen,width = 200,height = 46,placeholder_text="",border_width=3,fg_color="#096C82",bg_color="#5DA7B1",corner_radius=20,border_color="#FFFFFF")
    surname_entry = ctk.CTkEntry(font=font,master=m_data.screen,width = 200,height = 46,placeholder_text="",border_width=3,fg_color="#096C82",bg_color="#5DA7B1",corner_radius=20,border_color="#FFFFFF")
    country_entry = ctk.CTkEntry(font=font,master=m_data.screen,width = 218,height = 46,placeholder_text="",border_width=3,fg_color="#096C82",bg_color="#5DA7B1",corner_radius=20,border_color="#FFFFFF")
    place_entry = ctk.CTkEntry(font=font,master=m_data.screen,width = 218,height = 46,placeholder_text="",border_width=3,fg_color = "#096C82",bg_color="#5DA7B1",corner_radius=20,border_color="#FFFFFF")

    country_entry.place(x=38,y=150)
    place_entry.place(x=38,y=249)
    name_entry.place(x=38,y=348)
    surname_entry.place(x=38,y=447)

m_data.screen.resizable(False,False)
# створюємо кнопку при натисканні на неї викликається функція registration
background = ctk.CTkButton(master=m_data.screen,width=m_data.width,height=m_data.height,text="",border_width=5,fg_color="#5DA7B1",border_color="#096C82",hover= False,corner_radius=20)
background.place(x = 0,y = 0)




m_data.screen.iconbitmap(os.path.abspath(__file__+"/../../../icon.ico"))
def back():
    global text2,text3,text4,text5
    font = ctk.CTkFont(family=m_data.path,size=22,weight=("bold"))
    text2 = ctk.CTkLabel(font= font,master=m_data.screen,width=121,height=31,text="Прівище:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text2.place(x = 46,y = 405)

    text3 = ctk.CTkLabel(font= font, master=m_data.screen,width=87,height=31,text="Ім'я:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text3.place(x = 46,y = 306)


    text4 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text="Місто:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text4.place(x = 46,y = 207)

    text5 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text="Країна:",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text5.place(x = 46,y = 108)
# back()
font = ctk.CTkFont(family=m_data.path,size=18,weight=("bold"))

# transparent
# background_corner_colors=(9,108,130)
#ctk.Entry - текстовое поле
# enter()
# registration()