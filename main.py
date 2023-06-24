# # python main2.py
from utils import random_headers, cleanup_cache
from parsers import pravda_parser, e_pravda_parser, integrPravda_parser, lifePravda_parser
from settings import settings
import telebot
import requests
from bs4 import BeautifulSoup
import atexit
import time
import re
import random

class Tg:
    def __init__(self, api_token) -> None:
        # api_token = settings.API_TOKEN
        self.CHAT_ID = settings.CHAT_ID
        self.bot = telebot.TeleBot(api_token)
        self.control = Controller()
        # self.c_cache = cleanup_cache.cleanup_cachee()
        atexit.register(cleanup_cache.cleanup_cachee)

    def start_command(self, message):
        self.bot.reply_to(message, "Hello! I'm News Bot!")
        while True:
            content_of_post = self.control.main_controller()
            if content_of_post is not None:
                header = f"*{content_of_post[1]}*\n\n"
                body = content_of_post[0]
                self.bot.send_message(chat_id=self.CHAT_ID, text=header + body, parse_mode="Markdown")
                try:
                    cleanup_cache.cleanup_cachee()
                except:
                    pass
            else:
                time.sleep(random.randrange(120, 180))
                continue

    def start_bot(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.start_command(message)
        
        self.bot.polling()

class Controller:
    def __init__(self) -> None:
        self.time_bank = []
        self.timeSetBank = set()
        self.timeSize = []
        self.middleNight = False
        self.new_news_checker = False
        self.random_headers = random_headers.ffakeHeaders.randomH()
        self.main_link = 'https://www.pravda.com.ua/rus/news/'

    def request(self):
        for _ in range(7):
            try:
                r = requests.get(self.main_link, headers=self.random_headers)
                print(r.status_code)
                if r.status_code == 200:
                    return r
                else:
                    time.sleep(3)
                    continue
                
            except Exception as ex:
                print(f"main__49___{ex}")
                time.sleep(3)
                continue

    def link_extracter(self, r):
        try:
            soup = BeautifulSoup(r.text, 'lxml')
            try:
                aBlock = soup.find('div', class_='article_content').find('a').get('href')
            except:
                aBlock = ''
            try:
                timeBlock = soup.find('div', class_='article_time')
                realTimeFull = timeBlock.get_text().strip()
            except:
                realTimeFull = ''
            try:
                match = re.search(r'https://', aBlock)
                a_new_link = match.string
            except:
                a_new_link = f"https://www.pravda.com.ua{aBlock}"
            # print(a_new_link)
        except Exception as ex:
            print(f'main_74__{ex}')
            return None, None
        if aBlock == '':
            return None, None

        try:
            return a_new_link, realTimeFull
        except:
            return None, None

    def time_manager(self, realTimeFull):
        middleNight = False
        realTimeH = realTimeFull.split(':')[0]
        self.time_bank.append(realTimeFull)

        if len(self.time_bank) == 1:
            flag_first_time = True
        else:
            flag_first_time = False

        if realTimeH == "23":
            middleNight = True

        if realTimeH == "00" and middleNight == True:
            self.timeSetBank = set()
            self.timeSize = []
            self.time_bank = []
            middleNight = False
        self.timeSetBank.add(realTimeFull)
        self.timeSize.append(len(self.timeSetBank))

        if flag_first_time == True:
            return True
        try:
            if self.timeSize[-1] - self.timeSize[-2] != 0:
                return True
        except:
            pass

        return False

    def link_manager(self, a_new_link):
        result = None
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

        if pravdaComUa:
            # print('pravda')
            result = pravda_parser.pravdaCom(a_new_link, self.random_headers)
        elif ePravdaComUa:
            # print('ePravda')
            result = e_pravda_parser.ePravdaCom(a_new_link, self.random_headers)
        elif integrationComUa:
            # print('integration')
            result = integrPravda_parser.integrationCom(a_new_link, self.random_headers)
        elif lifePravdaComUa:
            # print('lifePravda')
            result = lifePravda_parser.lifePravdaCom(a_new_link, self.random_headers)
        else:
            pass
            # print('something else')

        return result

    def main_controller(self):
        r = self.request()
        result = None
        a_new_link, realTimeFull = self.link_extracter(r)
        new_news_checker = False
        if a_new_link != None and realTimeFull != None:
            new_news_checker = self.time_manager(realTimeFull)
        if new_news_checker == True:
            result = self.link_manager(a_new_link)

        return result

def main():
    api_token = settings.API_TOKEN
    tg_api = Tg(api_token)
    tg_api.start_bot()

if __name__ == "__main__":
    main()

