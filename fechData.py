from imports import *
from errorData import ErrorUrl
from user.getuser import getuser

def DataUrl():
    user = getuser()
    
    try :
        response = requests.post('http://localhost:5000/api',params={
            'name' : user,
            'status' : True
        })
        data = response.json()

        isrun = data['user']['result']['run']
        if (isrun):
            url = data['user']['url']
            return url
        
        if(response.status_code == 500 or 400):
            raise Exception(data)    
           
    except Exception :
       ErrorUrl(user)
DataUrl()