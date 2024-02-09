import modules.data_base as m_data
import customtkinter as ctk
import modules.data.values as d_values
import modules.data.table as d_table
import modules.data.column as d_column
#import modules.ctk.mini as ct_mini
from PIL import Image
import os
import modules.ctk.registration as m_reg
import modules.ctk.big_screen as ct_bg
# m_data.screen.geometry(f"{m_data.width}x{m_data.height}+{m_data.screen.winfo_screenwidth()//2-m_data.width//2}+{m_data.screen.winfo_screenheight()//2-m_data.width//2}")

def create():
    global text1,exit,text6,text7,text8,text9,button,text10
    m_data.status = "start"
    m_data.screen.title("Особистий кабінет")


    font = ctk.CTkFont(family=m_data.path,size=28,weight=("bold"))

    text1 = ctk.CTkLabel(font=font,master=m_data.screen,width=380,height=55,text="Особисий кабінет",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")

    text1.place(x = 38,y = 42)

    img = ctk.CTkImage(dark_image=Image.open(os.path.abspath(__file__ +"/../../../images/left-arrow_10559390.png")))

    exit = ctk.CTkButton(command= delete,master=m_data.screen,image=img,width= 28,height= 29,text="",bg_color="#5DA7B1",fg_color="#5DA7B1",hover=False)
    exit.place(x = 409,y = 20)

    text6 = ctk.CTkLabel(font= font,master=m_data.screen,width=121,height=31,text=d_values.get_value("Users",m_data.cursor,"surname"),text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text6.place(x = 119,y = 455)

    text7 = ctk.CTkLabel(font= font, master=m_data.screen,width=87,height=31,text=d_values.get_value("Users",m_data.cursor,"name"),text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text7.place(x = 121,y = 352)


    text8 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text=d_values.get_value("Users",m_data.cursor,"place"),text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text8.place(x = 121,y = 256)

    text9 = ctk.CTkLabel(font= font,master=m_data.screen,width=87,height=31,text=d_values.get_value("Users",m_data.cursor,"country"),text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1")
    text9.place(x = 119,y = 157)


    font = ctk.CTkFont(family=m_data.path,size=18,weight=("bold"))

    button = ctk.CTkButton(font= font,command= next,master=m_data.screen,width=218,height=46,text="Перейти до додатку",border_width=3,fg_color="#096C82", border_color= "#FFFFFF",text_color="#FFFFFF",corner_radius=20,bg_color="#5DA7B1")
    button.place(x = 119,y = 546)

    font = ctk.CTkFont(family=m_data.path,size=12)

    text10 = ctk.CTkButton(font= font,master=m_data.screen,width=36,height=13,text="Вихід",text_color="#FFFFFF",bg_color="#5DA7B1",fg_color="#5DA7B1",hover=False,command=delete)
    text10.place(x = 370,y = 26)
def next():
    if len(m_data.list_api)==6:
        text1.destroy()
        text6.destroy()
        text7.destroy()
        text8.destroy()
        text9.destroy()
        text10.destroy()
        button.destroy()
        exit.destroy()
        m_reg.text2.destroy()
        m_reg.text3.destroy()
        m_reg.text4.destroy()
        m_reg.text5.destroy()
        #print(1)
        ct_bg.create()
        # m_reg.registration.destroy()
def delete():
    d_table.delete_table("Users",m_data.cursor)
    d_table.create_table("Users",("id", "INTEGER PRIMRY KEY"),m_data.cursor)
    d_column.add_column("Users",m_data.cursor,"reg","INTEGER")
    d_column.add_column("Users",m_data.cursor,"name","TEXT")
    d_column.add_column("Users",m_data.cursor,"surname","TEXT")
    d_column.add_column("Users",m_data.cursor,"country","TEXT")
    d_column.add_column("Users",m_data.cursor,"place","TEXT")
    # d_column.add_column("Users",m_data.cursor,"activate","BOOLEAN")
    # boolean
    text1.destroy()
    text6.destroy()
    text7.destroy()
    text8.destroy()
    text9.destroy()
    text10.destroy()
    button.destroy()
    exit.destroy()
    m_reg.enter()