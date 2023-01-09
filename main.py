from requests_html import HTMLSession
from bs4 import BeautifulSoup
import telebot
from telebot import types
import time
import datetime 
import re
import random

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

time_bank = []
timeSetBank = set()
timeSize = []
middleNight = 0
flag = False
mes = ''
result = []
API_KEY = '5826732776:AAHWGm-qmTINd9rTJ7CGtFbDLlRIZKSkKUU'
# sonnik
# API_KEY = '5760534771:AAF82hGix86uOfv8sc0ag9HitREfLfoDCds'
# teos
chat_id = '-1001579866760'
# Ukr_Pravda_News chanel
# python teos_news.py
session = HTMLSession()

def newsCapturer(): 
        # print('hellooo')
        global flag           
        try:
            r = session.get('https://www.pravda.com.ua/rus/news/', headers=HEADERS)
            soup = BeautifulSoup(r.text, 'lxml')
            timeBlock = soup.find('div', class_='article_time')
            aBlock = soup.find('div', class_='article_content').find('a').get('href')
            try:         
                match = re.search(r'https://', aBlock)
                a_new_link = match.string       
            except: 
                a_new_link = f"https://www.pravda.com.ua{aBlock}"              
            
            if datetime.datetime.now().strftime("%H") == "00" and middleNight == 1:                                
                timeSetBank.clear()
                timeSize.clear()
                middleNight == 0
            if datetime.datetime.now().strftime("%H") == "23":
                middleNight == 1      
            
            if len(timeSize) != 0:                
                timeSetBank.add(timeBlock.get_text())
                timeSize.append(len(timeSetBank))                           
                if timeSize[-1] - timeSize[-2] != 0:
                    flag = True
                    print('goal')
                    hrefsControler(a_new_link)
                else:
                    print('retry')
                    flag = False
                    time.sleep(random.randrange(119,141))
                    newsCapturer()                     
            else:
                flag = True 
                print('first commit')           
                timeSetBank.add(timeBlock.get_text())
                timeSize.append(len(timeSetBank))                
                hrefsControler(a_new_link)
                    
        except:
            print('somth bad')
            time.sleep(random.randrange(58,69))
            newsCapturer() 
   
def hrefsControler(a_new_link):   
    pravdaComUa = ''
    ePravdaComUa = ''
    integrationComUa = ''
    lifePravdaComUa = ''    
    try:         
        match = re.search(r'https://www.pravda.com.ua', a_new_link)
        pravdaComUa = match.string         
    
    except: 
        pravdaComUa = ''
        
    try:         
        match = re.search(r'https://www.epravda.com.ua', a_new_link)
        ePravdaComUa = match.string         
    
    except: 
        ePravdaComUa = ''
    
    try:         
        match = re.search(r'https://www.eurointegration.com.ua', a_new_link)
        integrationComUa = match.string         
    
    except: 
        integrationComUa = ''
        
    try:         
        match = re.search(r'https://life.pravda.com.ua', a_new_link)
        lifePravdaComUa = match.string         
    
    except: 
        lifePravdaComUa = ''        
            
    if pravdaComUa != '':
        print('pravda')
        pravdaCom(a_new_link)   
        
    elif ePravdaComUa != '':
        print('ePravda')
        ePravdaCom(a_new_link)
    elif integrationComUa != '':
        print('integration')
        integrationCom(a_new_link)
    elif lifePravdaComUa != '':
        print('lifePravda')
        lifePravdaCom(a_new_link)
    else:
        print('something else')

def pravdaCom(a_new_link):
    global result
    global mes
    result = []
    mes = ''
    counter = 0
    while(True): 
        try:  
            r = session.get(f'{a_new_link}', headers=HEADERS)
            # r = session.get(f'https://www.pravda.com.ua/rus/news/2022/12/30/7383053/', headers=HEADERS)    
            soup = BeautifulSoup(r.text, 'lxml')
            dataInfo =''
            text = ''    
            try:
                h1 = soup.find('h1', class_='post_title').get_text().strip()
            except:
                h1 = ''        
            try:
                author = soup.find('div', class_='post_time').find('span', clas_='post_author').get_text()
            except:
                author = ''        
            try:
                postData = soup.find('div', class_='post_time').get_text()
            except:
                postData = ''        
            dataInfo = author + ' ' + postData
            try:
                img = soup.find('img', class_='post_photo_news_img').get('src')
            except:
                img = '' 
            try:
                post2 = soup.find('div', class_='post_text').find_all('li')
                for item2 in post2:
                    text+=item2.get_text() + '\n'  
            except:
                print('exPost2')    
            try:
                post = soup.find('div', class_='post_text').find_all('p')        
                for item1 in post:
                    text+=item1.get_text() + '\n'                
            except:
                print('exPost')
                
            result.append({
                'header': h1,
                'dataInfo': dataInfo,
                'img': img,
                'text': text,
                'titleLink': a_new_link      
            })    
            mes = result[0]['dataInfo'] + '\n' + result[0]['img'] + '\n' + result[0]['text'] + '\n' + result[0]['titleLink'] + '\n'
            counter = 0
            break
            # return result, mes
        except:
            print('pravda ex')
            counter += 1
            if counter == 7:
                counter = 0
                break
            time.sleep(2)
            continue
        
def ePravdaCom(a_new_link):
    global result
    global mes
    result = []
    mes = ''
    counter = 0
    while(True):
        try:    
            r = session.get(f'{a_new_link}', headers=HEADERS)
            # r = session.get(f'https://www.epravda.com.ua/rus/news/2023/01/3/695671/', headers=HEADERS)    
            soup = BeautifulSoup(r.text, 'lxml')
            dataInfo =''
            text = ''    
            try:
                h1 = soup.find('h1', class_='post__title').get_text().strip()
            except:
                h1 = ''        
            try:
                author = soup.find('div', class_='post__time').find('span', clas_='post__author').get_text()
            except:
                author = ''        
            try:
                postData = soup.find('div', class_='post__time').get_text()
            except:
                postData = ''        
            dataInfo = author + ' ' + postData
            try:
                img = soup.find('img', class_='post_photo_news_img').get('src')
            except:
                img = '' 
            try:
                post2 = soup.find('div', class_='post__text').find_all('li')
                for item2 in post2:
                    text+=item2.get_text() + '\n'
            except:
                print('exPost2')    
            try:
                post = soup.find('div', class_='post__text').find_all('p')        
                for item1 in post:
                    text+=item1.get_text() + '\n'                
            except:
                print('exPost')
                
            result.append({
                'header': h1,
                'dataInfo': dataInfo,
                'img': img,
                'text': text,
                'titleLink': a_new_link,        
            })
            mes = result[0]['dataInfo'] + '\n' + result[0]['img'] + '\n' + result[0]['text'] + '\n' + result[0]['titleLink'] + '\n'
            counter = 0
            break
            # return result, mes
        except:
            print('ePravda ex')
            counter += 1
            if counter == 7:
                counter = 0
                break
            time.sleep(2)
            continue
        
def integrationCom(a_new_link):
    global result
    global mes
    result = []
    mes = ''
    counter = 0
    while(True): 
        try:   
            r = session.get(f'{a_new_link}', headers=HEADERS)
            # r = session.get(f'https://www.eurointegration.com.ua/rus/news/2023/01/3/7153513/', headers=HEADERS)    
            soup = BeautifulSoup(r.text, 'lxml')
            text = ''    
            try:
                h1 = soup.find('h1', class_='post__title').get_text().strip()
            except:
                h1 = ''          
            try:
                postData = soup.find('div', class_='post__time').get_text()
            except:
                postData = ''  
            try:
                img = soup.find('img', class_='post_photo_news_img').get('src')
            except:
                img = ''    
            try:
                post2 = soup.find('div', class_='post__text').find_all('li')
                for item2 in post2:
                    text+=item2.get_text() + '\n' 
            except:
                print('exPost2')    
            try:
                post = soup.find('div', class_='post__text').find_all('p')        
                for item1 in post:
                    text+=item1.get_text() + '\n'                
            except:
                print('exPost')
                
            result.append({        
                'header': h1,
                'dataInfo': postData,
                'img': img,
                'text': text,
                'titleLink': a_new_link               
            })    
            mes = result[0]['dataInfo'] + '\n' + result[0]['img'] + '\n' + result[0]['text'] + '\n' + result[0]['titleLink'] + '\n'
            counter = 0
            break
            # return result, mes
        except:
            print('integration ex')
            counter += 1
            if counter == 7:
                counter = 0
                break
            time.sleep(2)
            continue
def lifePravdaCom(a_new_link):
    global result
    global mes
    result = []
    mes = ''
    counter = 0
    while(True):  
        try:  
            r = session.get(f'{a_new_link}', headers=HEADERS)
            # r = session.get(f'https://life.pravda.com.ua/society/2023/01/3/252136/', headers=HEADERS)    
            soup = BeautifulSoup(r.text, 'lxml')
            dataInfo =''
            text = ''    
            try:
                h1 = soup.find('h1', class_='page-heading').get_text().strip()
            except:
                h1 = ''        
            try:
                author = soup.find('a', class_='article-announcement-text').find('span', class_='autor-name').get_text()
            except:
                author = ''        
            try:
                postData = soup.find('div', class_='data-block').find('span', class_='data').get_text()
            except:
                postData = ''        
            dataInfo = author + ' ' + postData    
            try:
                post = soup.find('article', class_='article').find_all('p')        
                for item1 in post:
                    text+=item1.get_text() + '\n'                 
            except:
                post = ''        
            try:
                post2 = soup.find('article', class_='article').find_all('li')
                for item2 in post2:
                    text+=item2.get_text() + '\n' 
            except:
                post2 = ''      
            try:
                video = soup.find('article', class_='article').find('iframe').get('src')  
            except:
                video = ''   
                
            result.append({        
                'header': h1,
                'dataInfo': dataInfo,
                'video': video,
                'text': text,
                'titleLink': a_new_link,      
            })    
            mes = result[0]['dataInfo'] + '\n' + result[0]['video'] + '\n' + result[0]['text'] + '\n' + result[0]['titleLink'] + '\n'
            counter = 0
            break
            # return result, mes
        except:
            print('life ex')
            counter += 1
            if counter == 7:
                counter = 0
                break
            time.sleep(2)
            continue

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start']) 

def start(message):    
    while(True):
        global result
        global mes 
        global flag     
        time.sleep(2)        
        print(str('test' + result[0]['header'] + 'hhbhbhbh'))
        print(flag)
        print('first away')              
        if flag == True:           
            try:
                # bot.reply_to(message, f"*{(name.result[0]['header'])}*\n\n{name.mes}\n\n", parse_mode="Markdown")
                bot.send_message(chat_id, f"*{(result[0]['header'])}*\n\n{mes}\n\n", parse_mode="Markdown")
                flag = False               
                # await bot.send_message(id_channel, f"{hbold(name.result[0]['header'])}\n\n{name.mes}\n\n")
                print('success')                
            except:
                print('connection error')
                time.sleep(10)
                try:
                #    bot.reply_to(message, f"*{(name.result[0]['header'])}*\n\n{name.mes}\n\n", parse_mode="Markdown")
                   bot.send_message(chat_id, f"*{(result[0]['header'])}*\n\n{mes}\n\n", parse_mode="Markdown")
                except:
                    print('sec connection error') 
                    time.sleep(20)  
                    try:
                #    bot.reply_to(message, f"*{(name.result[0]['header'])}*\n\n{name.mes}\n\n", parse_mode="Markdown")
                        bot.send_message(chat_id, f"*{(result[0]['header'])}*\n\n{mes}\n\n", parse_mode="Markdown")
                    except:
                        print('third connection error')                  
            flag = False
        print('away')        
        time.sleep(random.randrange(119,141))
        newsCapturer()

def main(): 
    newsCapturer()   
    bot.polling() 
        
if __name__ == "__main__":
    main()  

# python main.py