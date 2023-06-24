import requests
from bs4 import BeautifulSoup
import random 
import time 

def lifePravdaCom(a_new_link, headers):
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
                h1 = soup.find('h1', class_='page-heading').get_text().strip()
            except:
                h1 = ''  

            # try:
            #     author = soup.find('a', class_='article-announcement-text').find('span', class_='autor-name').get_text()
            # except:
            #     author = ''        
            try:
                postData = soup.find('div', class_='data-block').find('span', class_='data').get_text()
            except:
                postData = ''        
            # dataInfo = author + ' ' + postData    
            try:
                text = ''
                post = soup.find('article', class_='article').find_all('p')        
                for item1 in post:
                    text+=item1.get_text() + '\n'                 
            except:
                text = ''        
            try:
                post2 = soup.find('article', class_='article').find_all('li')
                for item2 in post2:
                    text+=item2.get_text() + '\n' 
            except:
                text = text      
            try:
                video = soup.find('article', class_='article').find('iframe').get('src')  
            except:
                video = ''   

            mes = postData + '\n' + video + '\n' + text + '\n' + a_new_link + '\n'
            break

        except:
            print('lifePravda ex')                
            time.sleep(random.randrange(2, 8))
            continue
    try:
        return [mes, h1]
    except:
        return None
