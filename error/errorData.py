from imports import *
from url import ROOT_DIR

def ErrorUrl (user,error):
        data = {
        "name" : user, 
        "date" : datetime.now(),
        "error" : error
        }

        with open(ROOT_DIR + '\\log.txt','w') as file:
            file.write(str(data))