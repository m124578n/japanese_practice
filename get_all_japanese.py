# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:19:53 2024

@author: TW000626
"""


from bs4 import BeautifulSoup
import requests


headers = {
    'authority': 'home.gamer.com.tw',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_ga=GA1.1.604202131.1706251873; ckHOME_visitor=99931727307337729; __cf_bm=UFcKYTMcu0gmV5yHwIeS_ftHZeayOO9l_qdlgGp0Eok-1709863980-1.0.1.1-A8Rpbv9PEmydMXF9jj4pt50P8k_.hqb5VJqVpavCydytKi00bpi6hKoaKx3Hx6XCnnrfy0BmGMKyV2Uzga7SUg; __gads=ID=2314eaa381ad1058:T=1706251873:RT=1709864381:S=ALNI_MYDcK2RlUce-rwcqfkg74TU-LMBrA; __gpi=UID=00000cf065625dd6:T=1706251873:RT=1709864381:S=ALNI_MZseyBZo3RFmGXrlsEtk6SJcJZP1g; __eoi=ID=e2503a12bd650827:T=1709863981:RT=1709864381:S=AA-AfjbibhFwnOtshYQ0-CdKZaM0; _ga_2Q21791Y9D=GS1.1.1709863981.2.1.1709864381.59.0.0; FCNEC=%5B%5B%22AKsRol9MiMuvMjrhlWVp_ejyNEyeL-p8uSklyk3Ke9UDvNp3Oo5vqKZHGQqRtjcho7qdDk6jO-XkXOXcOwv6jVb6Ik-EWHeyaBCmHKdCb64Czq9IQ3IUjUSGGTk2gXZ7fkSjqg4xrKyN4zpHusjjC5QR6q6RvHHT-w%3D%3D%22%5D%5D',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

params = {
    'sn': '3667405',
}

response = requests.get('https://home.gamer.com.tw/creationDetail.php', params=params, headers=headers)


soup = BeautifulSoup(response.text, 'html.parser')

# hira
soup.find_all('table')[1]
ans = []
for x in soup.find_all('table')[1].find_all('td'):
    temp = {}
    b = x.text.strip()
    if b:
        temp['moji'] = b[:1]
        temp['spell'] = b[1:]
        ans.append(temp)

# taku
soup.find_all('table')[2]
ans = []
for x in soup.find_all('table')[2].find_all('td'):
    temp = {}
    b = x.text.strip()
    if b:
        temp['moji'] = b[:1]
        temp['spell'] = b[1:]
        ans.append(temp)

# connect
soup.find_all('table')[3]
ans = []
for x in soup.find_all('table')[3].find_all('td'):
    temp = {}
    b = x.text.strip()
    if b:
        temp['moji'] = b[:2]
        temp['spell'] = b[2:]
        ans.append(temp)


soup.find_all('table')[4]
ans = []
for x in soup.find_all('table')[4].find_all('td'):
    temp = {}
    b = x.text.strip()
    if b:
        temp['moji'] = b[:1]
        temp['spell'] = b[1:]
        ans.append(temp)
        
        
soup.find_all('table')[5]
ans = []
for x in soup.find_all('table')[5].find_all('td'):
    temp = {}
    b = x.text.strip()
    if b:
        temp['moji'] = b[:1]
        temp['spell'] = b[1:]
        ans.append(temp)
        
soup.find_all('table')[6]
ans = []
for x in soup.find_all('table')[6].find_all('td'):
    temp = {}
    b = x.text.strip()
    if b:
        temp['moji'] = b[:2]
        temp['spell'] = b[2:]
        ans.append(temp)