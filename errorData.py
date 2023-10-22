from imports import *

def ErrorUrl (user):
    
    try: 
        response = requests.post('http://localhost:5000/api',{
          'name' : user
        })

        x = response.json()
        if(response.status_code == 500):
            raise Exception(x)
    except Exception as e:
        data = {
        "date" : datetime.now(),
        "error" : e
        }

        with open('log.txt','w') as file:
            file.write(str(data))