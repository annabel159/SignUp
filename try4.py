from pprint import pprint
import requests
from bs4 import BeautifulSoup as bs4

from config import username, password

cookies = {
    'checkCookiesEnabled': 'value',
    'APPSESSIONID': '2AFB85C1CF671CD7A1D21AAE6ED00C60',
    'token': 'K1735ZOHZT1KCDKN3XLOPOILBNX8DJCE',
    'portalSessionId': '6c28bd5f-e7ac-4e1f-a727-303ff04b0ad3',
    '_ga': 'GA1.2.1977851140.1608402450',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8,nl;q=0.7',
}

params = (
    ('portal', '4f1ab610-d83f-11e8-a0ab-bea55ce933d8'),
)

url = 'https://portaal1.rztienen.be:8443/portal/PortalSetup.action'

with requests.Session() as session:
    response = session.get(url, headers=headers, params=params, cookies=cookies)
    response.text
    html_bytes = response.text
    soup = bs4(html_bytes, 'lxml')
    soup = bs4(response.content, "html.parser")
    token = soup.select_one('input[name=token]')['value']
    portal = soup.select_one('input[name=portal]')['value']

    print('portal = ', portal)
    print('token = ', token)

    data = {'user.username': username,
            'user.password': password,
            'portal': portal,
            'token': token,
            'response': response}

    r_post = session.post(url, data=data)
    pprint(r_post.text)

    with open('index.html', 'w') as f:
        f.write(response.text)

#response = requests.get('https://portaal1.rztienen.be:8443/portal/PortalSetup.action', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://portaal1.rztienen.be:8443/portal/PortalSetup.action?portal=4f1ab610-d83f-11e8-a0ab-bea55ce933d8', headers=headers, cookies=cookies)
