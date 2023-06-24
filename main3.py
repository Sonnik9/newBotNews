# from requests_html import HTMLSession
# from bs4 import BeautifulSoup
# import telebot
# # from telebot import types
# import time
# import datetime 
# import re
# import random
# from fake_useragent import UserAgent
# ua = UserAgent()


# time_bank = []
# timeSetBank = set()
# timeSize = []
# middleNight = 0
# flag = False
# mes = ''
# result = []
# API_KEY = '5826732776:AAHWGm-qmTINd9rTJ7CGtFbDLlRIZKSkKUU'
# # API_KEY = '6010432519:AAEgyTGCwCw-bZ8vWLnYmdLbcuLQ_ugfj2s'
# # sonnik
# # API_KEY = '5760534771:AAF82hGix86uOfv8sc0ag9HitREfLfoDCds'
# # teos
# chat_id = '-1001579866760'
# # Ukr_Pravda_News chanel
# # python teos_news.py
# session = HTMLSession()

# bot = telebot.TeleBot(API_KEY)
# @bot.message_handler(commands=['start']) 

# def start(message):
#     global result
#     global mes 
#     global flag
#     print('hello')

#     while(True):
#         headers = {
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#             'user-agent': ua.random
#         }  
#         # print(headers)     
          
#         time.sleep(2)  
#         try:        
#            print(str('test' + result[0]['header'] + 'hhbhbhbh'))
#         except:
#            print('empty result')
#            newsCapturer(headers)
#            time.sleep(2) 
#         print(flag)
#         print('first away')              
#         if flag == True:           
#             try:
#                 # bot.reply_to(message, f"*{(name.result[0]['header'])}*\n\n{name.mes}\n\n", parse_mode="Markdown")
#                 bot.send_message(chat_id, f"*{(result[0]['header'])}*\n\n{mes}\n\n", parse_mode="Markdown")
#                 flag = False               
#                 # await bot.send_message(id_channel, f"{hbold(name.result[0]['header'])}\n\n{name.mes}\n\n")
#                 print('success')                
#             except:
#                 print('connection error')
#                 time.sleep(10)
#                 try:
#                 #    bot.reply_to(message, f"*{(name.result[0]['header'])}*\n\n{name.mes}\n\n", parse_mode="Markdown")
#                    bot.send_message(chat_id, f"*{(result[0]['header'])}*\n\n{mes}\n\n", parse_mode="Markdown")
#                    flag = False
#                    print('success2')
#                 except:
#                     print('sec connection error') 
#                     time.sleep(20)  
#                     try:
#                 #    bot.reply_to(message, f"*{(name.result[0]['header'])}*\n\n{name.mes}\n\n", parse_mode="Markdown")
#                         bot.send_message(chat_id, f"*{(result[0]['header'])}*\n\n{mes}\n\n", parse_mode="Markdown")
#                         flag = False
#                         print('success3')
#                     except:
#                         print('third connection error')                  
            
#         # print('away')        
#         time.sleep(random.randrange(119,141))
#         newsCapturer(headers)
#         # newsCapturer()

# def newsCapturer(headers): 
#         global flag
#         global middleNight           
#         try:
#             r = session.get('https://www.pravda.com.ua/rus/news/', headers=headers)
#             soup = BeautifulSoup(r.text, 'lxml')
#             timeBlock = soup.find('div', class_='article_time')
#             aBlock = soup.find('div', class_='article_content').find('a').get('href')
#             realTime = timeBlock.get_text().strip().split(':')[0]
#             try:         
#                 match = re.search(r'https://', aBlock)
#                 a_new_link = match.string       
#             except: 
#                 a_new_link = f"https://www.pravda.com.ua{aBlock}"
#             print(realTime)
#             # print(datetime.datetime.now().strftime("%H"))
#             # if datetime.datetime.now().strftime("%H") == "21":
#             #     print(len(timeSetBank))
#             #     middleNight = 1          
#             # if datetime.datetime.now().strftime("%H") == "22" and middleNight == 1:                                
#             #     timeSetBank.clear()
#             #     timeSize.clear()
#             #     middleNight = 0

#             if realTime == "23":
#                 print('true time')
#                 print(len(timeSetBank))
#                 middleNight = 1 
#                 # print(timeSetBank)       
#             if realTime == "00" and middleNight == 1:                                
#                 timeSetBank.clear()
#                 timeSize.clear()
#                 print(f"{realTime}__len timesetBank: {len(timeSetBank)}")
#                 middleNight = 0                           
            
#             if len(timeSize) != 0:                
#                 timeSetBank.add(timeBlock.get_text())
#                 timeSize.append(len(timeSetBank))                           
#                 if timeSize[-1] - timeSize[-2] != 0:
#                     flag = True
#                     print('goal')
#                     hrefsControler(a_new_link, headers)
#                 else:
#                     print('retry')
#                     time.sleep(random.randrange(119,141))
#                     newsCapturer(headers)                     
#             else:
#                 flag = True 
#                 print('first commit')           
#                 timeSetBank.add(timeBlock.get_text())
#                 timeSize.append(len(timeSetBank))                
#                 hrefsControler(a_new_link, headers)
                    
#         except:
#             print('somth bad')
#             time.sleep(random.randrange(58,69))
#             newsCapturer(headers) 
   
# def hrefsControler(a_new_link, headers):   
#     pravdaComUa = ''
#     ePravdaComUa = ''
#     integrationComUa = ''
#     lifePravdaComUa = ''    
#     try:         
#         match = re.search(r'https://www.pravda.com.ua', a_new_link)
#         pravdaComUa = match.string         
    
#     except: 
#         pravdaComUa = ''
        
#     try:         
#         match = re.search(r'https://www.epravda.com.ua', a_new_link)
#         ePravdaComUa = match.string         
    
#     except: 
#         ePravdaComUa = ''
    
#     try:         
#         match = re.search(r'https://www.eurointegration.com.ua', a_new_link)
#         integrationComUa = match.string         
    
#     except: 
#         integrationComUa = ''
        
#     try:         
#         match = re.search(r'https://life.pravda.com.ua', a_new_link)
#         lifePravdaComUa = match.string         
    
#     except: 
#         lifePravdaComUa = ''        
            
#     if pravdaComUa != '':
#         print('pravda')
#         pravdaCom(a_new_link, headers)   
        
#     elif ePravdaComUa != '':
#         print('ePravda')
#         ePravdaCom(a_new_link, headers)
#     elif integrationComUa != '':
#         print('integration')
#         integrationCom(a_new_link, headers)
#     elif lifePravdaComUa != '':
#         print('lifePravda')
#         lifePravdaCom(a_new_link, headers)
#     else:
#         print('something else')

# def pravdaCom(a_new_link, headers):
#     global result
#     global mes
#     result = []
#     mes = ''
#     counter = 0
#     while(True): 
#         try:  
#             r = session.get(f'{a_new_link}', headers=headers)
#             # print(r.status_code)
#             # r = session.get(f'https://www.pravda.com.ua/rus/news/2022/12/30/7383053/', headers=HEADERS)    
#             soup = BeautifulSoup(r.text, 'lxml')
#             # print(r.text)
#             dataInfo =''
#             text = ''    
#             try:
#                 h1 = soup.find('h1', class_='post_title').get_text().strip()
#             except:
#                 h1 = ''        
#             try:
#                 author = soup.find('div', class_='post_time').find('span', clas_='post_author').get_text()
#             except:
#                 author = ''        
#             try:
#                 postData = soup.find('div', class_='post_time').get_text()
#             except:
#                 postData = ''        
#             dataInfo = author + ' ' + postData
#             try:
#                 img = soup.find('img', class_='post_photo_news_img').get('src')
#             except:
#                 img = '' 
#             try:
#                 post2 = soup.find('div', class_='post_text').find_all('li')
#                 for item2 in post2:
#                     text+=item2.get_text() + '\n'  
#             except:
#                 print('exPost2')    
#             try:
#                 post = soup.find('div', class_='post_text').find_all('p')        
#                 for item1 in post:
#                     text+=item1.get_text() + '\n'                
#             except:
#                 print('exPost')
                
#             result.append({
#                 'header': h1,
#                 'dataInfo': dataInfo,
#                 'img': img,
#                 'text': text,
#                 'titleLink': a_new_link      
#             })    
#             mes = result[0]['dataInfo'] + '\n' + result[0]['img'] + '\n' + result[0]['text'] + '\n' + result[0]['titleLink'] + '\n'
#             counter = 0
#             # print(mes)
#             break
#             # return result, mes
#         except:
#             print('pravda ex')
#             counter += 1
#             if counter == 7:
#                 counter = 0
#                 break
                
#             time.sleep(random.randrange(2, 8))
#             continue
        
# def ePravdaCom(a_new_link, headers):
#     global result
#     global mes
#     result = []
#     mes = ''
#     counter = 0
#     while(True):
#         try:    
#             r = session.get(f'{a_new_link}', headers=headers)
#             # r = session.get(f'https://www.epravda.com.ua/rus/news/2023/01/3/695671/', headers=HEADERS)    
#             soup = BeautifulSoup(r.text, 'lxml')
#             dataInfo =''
#             text = ''    
#             try:
#                 h1 = soup.find('h1', class_='post__title').get_text().strip()
#             except:
#                 h1 = ''        
#             try:
#                 author = soup.find('div', class_='post__time').find('span', clas_='post__author').get_text()
#             except:
#                 author = ''        
#             try:
#                 postData = soup.find('div', class_='post__time').get_text()
#             except:
#                 postData = ''        
#             dataInfo = author + ' ' + postData
#             try:
#                 img = soup.find('img', class_='post_photo_news_img').get('src')
#             except:
#                 img = '' 
#             try:
#                 post2 = soup.find('div', class_='post__text').find_all('li')
#                 for item2 in post2:
#                     text+=item2.get_text() + '\n'
#             except:
#                 print('exPost2')    
#             try:
#                 post = soup.find('div', class_='post__text').find_all('p')        
#                 for item1 in post:
#                     text+=item1.get_text() + '\n'                
#             except:
#                 print('exPost')
                
#             result.append({
#                 'header': h1,
#                 'dataInfo': dataInfo,
#                 'img': img,
#                 'text': text,
#                 'titleLink': a_new_link,        
#             })
#             mes = result[0]['dataInfo'] + '\n' + result[0]['img'] + '\n' + result[0]['text'] + '\n' + result[0]['titleLink'] + '\n'
#             counter = 0
#             break
#             # return result, mes
#         except:
#             print('ePravda ex')
#             counter += 1
#             if counter == 7:
#                 counter = 0
#                 break
#             time.sleep(random.randrange(2, 8))
#             continue
        
# def integrationCom(a_new_link, headers):
#     global result
#     global mes    
#     result = []
#     mes = ''
#     counter = 0
#     while(True): 
#         try:   
#             r = session.get(f'{a_new_link}', headers=headers)
#             # r = session.get(f'https://www.eurointegration.com.ua/rus/news/2023/01/3/7153513/', headers=HEADERS)    
#             soup = BeautifulSoup(r.text, 'lxml')
#             text = ''    
#             try:
#                 h1 = soup.find('h1', class_='post__title').get_text().strip()
#             except:
#                 h1 = ''          
#             try:
#                 postData = soup.find('div', class_='post__time').get_text()
#             except:
#                 postData = ''  
#             try:
#                 img = soup.find('img', class_='post_photo_news_img').get('src')
#             except:
#                 img = ''    
#             try:
#                 post2 = soup.find('div', class_='post__text').find_all('li')
#                 for item2 in post2:
#                     text+=item2.get_text() + '\n' 
#             except:
#                 print('exPost2')    
#             try:
#                 post = soup.find('div', class_='post__text').find_all('p')        
#                 for item1 in post:
#                     text+=item1.get_text() + '\n'                
#             except:
#                 print('exPost')
                
#             result.append({        
#                 'header': h1,
#                 'dataInfo': postData,
#                 'img': img,
#                 'text': text,
#                 'titleLink': a_new_link               
#             })    
#             mes = result[0]['dataInfo'] + '\n' + result[0]['img'] + '\n' + result[0]['text'] + '\n' + result[0]['titleLink'] + '\n'
#             counter = 0
#             break
#             # return result, mes
#         except:
#             print('integration ex')
#             counter += 1
#             if counter == 7:
#                 counter = 0
#                 break
#             time.sleep(random.randrange(2, 8))
#             continue

# def lifePravdaCom(a_new_link, headers):
#     global result
#     global mes
#     result = []
#     mes = ''
#     counter = 0
#     while(True):  
#         try:  
#             r = session.get(f'{a_new_link}', headers=headers)
#             # r = session.get(f'https://life.pravda.com.ua/society/2023/01/3/252136/', headers=HEADERS)    
#             soup = BeautifulSoup(r.text, 'lxml')
#             dataInfo =''
#             text = ''    
#             try:
#                 h1 = soup.find('h1', class_='page-heading').get_text().strip()
#             except:
#                 h1 = ''        
#             try:
#                 author = soup.find('a', class_='article-announcement-text').find('span', class_='autor-name').get_text()
#             except:
#                 author = ''        
#             try:
#                 postData = soup.find('div', class_='data-block').find('span', class_='data').get_text()
#             except:
#                 postData = ''        
#             dataInfo = author + ' ' + postData    
#             try:
#                 post = soup.find('article', class_='article').find_all('p')        
#                 for item1 in post:
#                     text+=item1.get_text() + '\n'                 
#             except:
#                 post = ''        
#             try:
#                 post2 = soup.find('article', class_='article').find_all('li')
#                 for item2 in post2:
#                     text+=item2.get_text() + '\n' 
#             except:
#                 post2 = ''      
#             try:
#                 video = soup.find('article', class_='article').find('iframe').get('src')  
#             except:
#                 video = ''   
                
#             result.append({        
#                 'header': h1,
#                 'dataInfo': dataInfo,
#                 'video': video,
#                 'text': text,
#                 'titleLink': a_new_link,      
#             })    
#             mes = result[0]['dataInfo'] + '\n' + result[0]['video'] + '\n' + result[0]['text'] + '\n' + result[0]['titleLink'] + '\n'
#             counter = 0
#             break
#             # return result, mes
#         except:
#             print('life ex')
#             counter += 1
#             if counter == 7:
#                 counter = 0
#                 break
#             time.sleep(random.randrange(2, 8))
#             continue


# def main(): 
#     headers = {
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#         'user-agent': ua.random
#     }    
#     newsCapturer(headers) 
#     bot.infinity_polling() 
        
# if __name__ == "__main__":
#     main()  

# # python main.py


# from utils import random_headers
# from parsers import pravda_parser, e_pravda_parser, integrPravda_parser, lifePravda_parser
# from settings import settings
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# import telebot
# import requests
# from bs4 import BeautifulSoup
# import time
# import re
# import random

# class Tg:
#     def __init__(self, api_token) -> None:
#         self.CHAT_ID = settings.CHAT_ID
#         # self.bot = Bot(token=api_token, timeout=None)
#         self.bot = telebot.TeleBot(api_token, timeout=None)
#         # self.storage = MemoryStorage()
#         # self.dp = Dispatcher(self.bot, storage=self.storage)
#         # self.dp.register_message_handler(self.start_command, commands=['start'])
#         self.bot.register_message_handler(self.start_command, commands=['start'])
#         self.control = Controller()

#     def start_command(self, message):
#         self.bot.reply_to(message, "Hello! I'm News Bot!")
#         while True:
#             content_of_post = self.control.main_controller()
#             if content_of_post is not None:
#                 header = f"*{content_of_post[1]}*\n\n"
#                 body = content_of_post[0]
#                 self.bot.send_message(chat_id=self.CHAT_ID, text=header + body, parse_mode="Markdown")
#             else:
#                 time.sleep(random.randrange(120, 180))
#                 continue                

#     # async def start_bot(self):
#     #     await self.dp.start_polling()
#     def start_bot(self):
#         self.bot.infinity_polling()

# class Controller:
#     def __init__(self) -> None:
#         self.time_bank = []
#         self.timeSetBank = set()
#         self.timeSize = []
#         self.middleNight = False
#         self.new_news_checker = False
#         self.random_headers = random_headers.ffakeHeaders.randomH()
#         self.main_link = 'https://www.pravda.com.ua/rus/news/'  

#     def request(self):
#         for _ in range(7):
#             try:
#                 r = requests.get(self.main_link, headers=self.random_headers)
#                 if r.status_code == 200:
#                     return r
#                 else:
#                     time.sleep(3) 
#                     continue 
#             except Exception as ex:
#                 print(f"main__49___{ex}")   
#                 time.sleep(3)
#                 continue
    
#     def link_extracter(self, r):
#         try:
#             soup = BeautifulSoup(r.text, 'lxml')            
#             try:
#                 aBlock = soup.find('div', class_='article_content').find('a').get('href')
#             except:
#                 aBlock = ''
#             try:
#                 timeBlock = soup.find('div', class_='article_time')       
#                 realTimeFull = timeBlock.get_text().strip()               
#             except:
#                 realTimeFull = ''   
#             try:         
#                 match = re.search(r'https://', aBlock)
#                 a_new_link = match.string                       
#             except: 
#                 a_new_link = f"https://www.pravda.com.ua{aBlock}"
#             print(a_new_link)
#         except Exception as ex:
#             print(f'main_74__{ex}')
#             # time.sleep(random.randrange(58,69))
#             return None, None
#         try:
#             return a_new_link, realTimeFull
#         except:
#             return None, None
    
#     def time_manager(self, realTimeFull):
#         middleNight = False  
#         realTimeH = realTimeFull.split(':')[0]     
#         self.time_bank.append(realTimeFull)
        
#         if len(self.time_bank) == 1:
#             flag_first_time = True 
#         else:
#             flag_first_time = False

#         if realTimeH == "23":
#             middleNight = True
          
#         if realTimeH == "00" and middleNight == True:                                
#             self.timeSetBank = set()
#             self.timeSize = []
#             self.time_bank = []
#             middleNight = False 
#         self.timeSetBank.add(realTimeFull)
#         self.timeSize.append(len(self.timeSetBank))  

#         if flag_first_time == True:
#             return True               
#         # if len(self.timeSize) >= 2:   
#         try:                    
#             if self.timeSize[-1] - self.timeSize[-2] != 0:                 
#                 return True
#         except:
#             pass
    
#         return False
    
#     def link_manager(self, a_new_link):
#         result = None
#         pravdaComUa = ''
#         ePravdaComUa = ''
#         integrationComUa = ''
#         lifePravdaComUa = ''    
#         try:         
#             match = re.search(r'https://www.pravda.com.ua', a_new_link)
#             pravdaComUa = match.string       
#         except: 
#             pravdaComUa = ''
            
#         try:         
#             match = re.search(r'https://www.epravda.com.ua', a_new_link)
#             ePravdaComUa = match.string       
#         except: 
#             ePravdaComUa = ''
        
#         try:         
#             match = re.search(r'https://www.eurointegration.com.ua', a_new_link)
#             integrationComUa = match.string
#         except: 
#             integrationComUa = ''
            
#         try:         
#             match = re.search(r'https://life.pravda.com.ua', a_new_link)
#             lifePravdaComUa = match.string       
#         except: 
#             lifePravdaComUa = ''        
                
#         if pravdaComUa:
#             print('pravda')
#             result = pravda_parser.pravdaCom(a_new_link, self.random_headers)           
#         elif ePravdaComUa:
#             print('ePravda')
#             result = e_pravda_parser.ePravdaCom(a_new_link, self.random_headers)    
#         elif integrationComUa:
#             print('integration')
#             result = integrPravda_parser.integrationCom(a_new_link, self.random_headers)    
#         elif lifePravdaComUa:
#             print('lifePravda')
#             result = lifePravda_parser.lifePravdaCom(a_new_link, self.random_headers)    
#         else:
#             print('something else')
        
#         return result 

    
#     def main_controller(self):
#         r = self.request()
#         result = None
#         a_new_link, realTimeFull = self.link_extracter(r)
#         if a_new_link != None and realTimeFull != None:
#            new_news_checker = self.time_manager(realTimeFull)
#         if new_news_checker == True:
#             result = self.link_manager(a_new_link)

#         return result

# def tg_main():
#     api_token = settings.API_TOKEN
#     tg_api = Tg(api_token)
#     tg_api.start_bot()

# def main():
#     import asyncio
#     asyncio.run(tg_main())

# if __name__ == "__main__":
#     main()


