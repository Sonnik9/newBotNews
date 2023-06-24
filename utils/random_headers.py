from fake_useragent import UserAgent 
from random import choice

class FakeHeaders:

    def __init__(self):
        self.desktop_accept = [
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng;q=0.8,application/signed-exchange;v=b3;q=0.9;charset=UTF-8',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8,application/signed-exchange;v=b3',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8;q=0.7',
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8;q=0.7, Cache-Control: no-cache',
        ]
        self.uagent = UserAgent()


    def randomH(self):
        headers = {      
            'Accept': choice(self.desktop_accept), 
            'User-Agent': self.uagent.random
        }
        return headers
    
ffakeHeaders = FakeHeaders()
# print(ffakeHeaders.randomH())

# python -m utils.random_headers
# python random_headers.py
        

