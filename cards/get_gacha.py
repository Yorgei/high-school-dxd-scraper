import requests
import time
import json
import re
from lxml import etree, html
from bs4 import BeautifulSoup

# no haci here brotherman 
with open('cards/cookies.json', 'r') as cookie_file:
    cookie_data = json.load(cookie_file)

regex = r"\%2F(\d*\_.*.jpg)"

# I remember it not working without x-mbga-check-cookie but I don't know if it still requires it
cookies = {
    'x-mbga-check-cookie': '1',
    'sp_mbga_sid_12014827': cookie_data['cookie'],
}

# Basic headers from a request using Firefox developer tools. The only thing you really need is the User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Referer': 'http://g12014827.sp.pf.mbga.jp/?url=http%3A%2F%2Fmg.highschooldd.net%2Fsp%2Fmypage.html',
    'Upgrade-Insecure-Requests': '1',
}

try:
    with open('dump.json', 'r') as json_file:
        json_data = json.load(json_file)
except FileNotFoundError:
    print('List not found. Run get_base_ids.py to scrape list')
    exit()
except Exception as e:
    print('Unknown error', e)
    exit()

# remove url from card ids
card_list = [x.replace('http://cdn-prod.highschooldd.net/sp/image/cards/C/', '').replace('.png', '') for x in json_data]

session = requests.session()
# Do your loop here for evolutions etc etc
for card in card_list:
    try:
        session.cookies.update(cookies)
        url = f'https://g12014827.sp.pf.mbga.jp/?url=http%3A%2F%2Fmg.highschooldd.net%2Fsp%2Fgacha_card_detail%3Fcard_id%3D{card}%26lineup%3Dnormal'
        response = session.get(url, headers=headers)
        cookies['sp_mbga_sid_12014827'] = session.cookies.get_dict()['sp_mbga_sid_12014827']
        # Cookie debug
        if session.cookies.get_dict()['sp_mbga_sid_12014827'] != cookie_data['cookie']:
            with open('cards/cookie.txt', 'a') as ctxt:
                ctxt.write(session.cookies.get_dict()['sp_mbga_sid_12014827']+'\n')
        page = response.content
        soup = BeautifulSoup(page, 'html.parser')
        links = soup.find('div', class_='center mt10').find('img')['src']
        name = soup.find('ul', class_='colorPram2 mt15').string.strip()
        card_id = re.findall(regex, links)[0]
        # i wanna see whats wrong ya feel
        with open('test.html', 'wb') as f:
            f.write(response.content)
        try:
            print(name, card_id)
        except Exception as e:
            print(e)
            pass
    except Exception as e:
        print('Error at', card, e)