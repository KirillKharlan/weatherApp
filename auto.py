import modules.data_base  as m_data
import modules.data.values as d_val
# print()
if d_val.get_value("Users",m_data.cursor,"reg")!=list():
    import modules.ctk.mini as ct_mini
    import modules.ctk.big_screen as ct_big
    import customtkinter as ctk
m_data.data.commit()
m_data.data.close()
# import os
# import getpass
# username=getpass.getuser()
# path=os.path.abspath(__file__+"/../auto"+"/auto.exe")
# #print(path,'\n',__file__)
# bat_path=r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'%username
# with open(bat_path+"\\open.bat","w+") as file:
#     file.write(r'start "name" %s'%path)