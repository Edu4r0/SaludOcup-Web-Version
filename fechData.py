from imports import *
from url import  URL_API
from error.errorData import ErrorUrl
from user.getuser import getuser

def DataUrl():
    user = getuser()
    
    try :
        response = requests.post(URL_API,params={
            'name' : user,
            'status' : True
        })
        data = response.json()

        isrun = data['user']['run']

        if(response.status_code == 500 or 400):
            raise Exception(data)  
         
        if (isrun == True):
            url = data['user']['url']
            return url
        else:
            return
    except Exception as error:
       ErrorUrl(user, error.args)