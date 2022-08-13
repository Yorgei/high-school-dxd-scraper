import requests
import time
import json

cookies = {
    'x-mbga-check-cookie': '1',
    'sp_mbga_sid_12014827': '8',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Referer': 'http://g12014827.sp.pf.mbga.jp/?url=http%3A%2F%2Fmg.highschooldd.net%2Fsp%2Fmypage.html',
    # Requests sorts cookies= alphabetically
    'Upgrade-Insecure-Requests': '1',
}

params = {
    'url': 'http://mg.highschooldd.net/sp/gacha',
}

with open('dump.json', 'r') as json_file:
    json_data = json.load(json_file)

# remove url from card ids
card_list = [x.replace('http://cdn-prod.highschooldd.net/sp/image/cards/C/', '').replace('.png', '') for x in json_data]

while True:
    session = requests.session()
    session.cookies.update(cookies)
    response = session.get('http://g12014827.sp.pf.mbga.jp/', params=params, headers=headers)
    print(session.cookies.get_dict())
    print(session.cookies.get('sp_mbga_sid_12014827'))
    cookies['sp_mbga_sid_12014827'] = session.cookies.get_dict()['sp_mbga_sid_12014827']
    with open('test.html', 'wb') as f:
        f.write(response.content)

    time.sleep(300)