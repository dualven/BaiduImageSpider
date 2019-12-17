# encoding:utf-8
import requests 
# client_id 为官网获取的AK， client_secret 为官网获取的SK
def GetToken():
     host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=5z0AEZuoQCkIFkVPL9FYfz8c&client_secret=gfLn8oMEr1VEdlH5moPPTiHQ9MBPtidF';
     response = requests.get(host)
     print(response.json()['access_token']);
     if response:
        print(response.json())
        return response.json();
     else :
        return null;

if __name__ == '__main__':
  mytoken = GetToken()
