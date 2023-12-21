from imports import *

def ErrorUrl (user,error):
        data = {
        "name" : user, 
        "date" : datetime.now(),
        "error" : error
        }

        with open('C:\Temp\SaludOcup-Web-Version' + '\\log.txt','w') as file:
            file.write(str(data))