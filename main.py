import customtkinter 
# import modules.ctk.mini 
import modules.data_base as m_data
# import auto
import os 
#print(r"C:\Users\epi99\OneDrive\workTable")
try:
    #print(os.path.abspath(__file__+"/../auto/auto.exe"))
   # os.link(os.path.abspath(__file__+"/../auto/auto.exe"),os.path.abspath(__file__+"/../weather_app.lnk"))
    os.replace(os.path.abspath(__file__+"/../weather app.lnk"),r"C:\\Users\\epi99\\OneDrive\\Рабочий стол\\weather app.lnk")
except:
    pass#goodbye
import modules.data.column as d_c
import modules.data.table as d_t
import modules.data.values as d_v
d_t.create_table("Users",["id","INTEGER PRIMARY KEY"],m_data.cursor)
d_c.add_column("Users",m_data.cursor,"reg","INTEGER")
d_c.add_column("Users",m_data.cursor,"name","TEXT")
d_c.add_column("Users",m_data.cursor,"surname","TEXT")
d_c.add_column("Users",m_data.cursor,"country","TEXT")
d_c.add_column("Users",m_data.cursor,"place","TEXT")
import modules.ctk.registration as ctk_rg
ctk_rg.back()
ctk_rg.enter()
ctk_rg.registration()
#понятно, пока C:\Users\epi99\OneDrive\workTable
m_data.screen.mainloop()
m_data.data.commit()
m_data.data.close()
#пока
os.system(os.path.abspath(__file__+"/../auto/auto.exe"))