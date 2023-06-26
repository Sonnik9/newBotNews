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
            'Authority': 'simage4.pubmatic.com',
            'Method': 'GET',
            'Path': '/AdServer/SPug?partnerID=162179&gdpr=0&gdpr_consent=&us_privacy=',
            'Scheme': 'https',
            # 'Accept': '*/*',
            'Accept': choice(self.desktop_accept),
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'Cookie': 'KADUSERCOOKIE=E05A7041-80DD-4963-99F8-04A085B027F2; chkChromeAb67Sec=16; pi=162179:3; DPSync3=1688947200%3A241_235_201_245; SyncRTB3=1689033600%3A35%7C1688947200%3A56_251_220_161_13_7_46_54_21%7C1688860800%3A69',
            'Referer': 'https://ads.pubmatic.com/',
            'Sec-Ch-Ua': f'"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': "Linux",
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': self.uagent.random,
            # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        # headers = {      
        #     'Accept': choice(self.desktop_accept), 
        #     'User-Agent': self.uagent.random
        # }
        return headers
    
ffakeHeaders = FakeHeaders()
# print(ffakeHeaders.randomH())

# python -m utils.random_headers
# python random_headers.py
        

