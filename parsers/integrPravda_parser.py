import requests
from bs4 import BeautifulSoup
import random 
import time 

def integrationCom(a_new_link, headers):
    mes = ''
    # print(a_new_link)
    # print(type(headers))
    # try:
    #     headers = eval(headers)
    # except:
    #     headers = headers

    for _ in range(7): 
        try:
            r = requests.get(a_new_link, headers=headers)  
            if r.status_code != 200:
                time.sleep(3)
                continue    
            # print(r.status_code)      
            soup = BeautifulSoup(r.text, 'lxml')            
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
                text = ''
                post2 = soup.find('div', class_='post__text').find_all('li')
                for item2 in post2:
                    text+=item2.get_text() + '\n' 
            except:
                text = ''    
            try:
                post = soup.find('div', class_='post__text').find_all('p')        
                for item1 in post:
                    text+=item1.get_text() + '\n'                
            except:
                text = text

            mes = postData + '\n' + img + '\n' + text + '\n' + a_new_link + '\n'
            break

        except:
            print('integrationPravda ex')                
            time.sleep(random.randrange(2, 8))
            continue
    try:
        return [mes, h1]
    except:
        return None
