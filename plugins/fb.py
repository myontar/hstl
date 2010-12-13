# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="John"
__date__ ="$12.Ara.2010 01:09:59$"



class facebookapp():

    def __init__(self):
        self.page_id = "167795576589520"
        self.accesstoken = "167795576589520|MaR7cPhvD3fUzkvHbwAfLkqqO3Y"
    
    def send(self,url):
        try:
            import   urllib
            from google.appengine.api import urlfetch

           
            result = urlfetch.fetch(url)
           
            if result.status_code == 200:
                
                result = r.content
               
        except:
            pass
        
    def sendMessage(self,msg,pic=None,desc=None,link=None,token = None):
        import urllib
       
        if pic == None:
            if token == None:
                dec = urllib.urlencode({'msg':msg,'access_token':token,"uid":self.page_id,"format":"json"})
            else:
                dec = urllib.urlencode({'msg':msg,'access_token':token,"format":"json"})
            self.send("https://api.facebook.com/method/stream.publish?"+dec)
        else:
            from django.utils import simplejson as json

            att = {"href":link,'description':desc,'name':msg,"media":[{"type":'image','src':pic,"href":link}]}
            att = json.dumps(att)
            if token == None:
                # if token == None:
                token = self.accesstoken
                dec = urllib.urlencode({'msg':msg,'access_token':token,"uid":self.page_id,"format":"json","attachment":att})
            else:
                dec = urllib.urlencode({'msg':msg,'access_token':token,"format":"json","attachment":att})
                
            self.send("https://api.facebook.com/method/stream.publish?"+dec)


