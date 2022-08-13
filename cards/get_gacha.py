import requests

cookies = {
    'x-mbga-check-cookie': '1',
    'sp_mbga_sid_12014827': 'getfromfile',
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

response = requests.get('http://g12014827.sp.pf.mbga.jp/', params=params, cookies=cookies, headers=headers)
with open('test.html', 'wb') as f:
    f.write(response.content)