from pprint import pprint

import requests
from bs4 import BeautifulSoup as bs4

from config import username, password


def main():
    #url = 'https://portaal1.rztienen.be:8443'
    #url = 'https://portaal1.rztienen.be:8443/portal/PortalSetup.action?portal=4f1ab610-d83f-11e8-a0ab-bea55ce933d8&sessionId=0be1340a001bf5ecc91be25f&action=cwa&redirect=www.msftconnecttest.com%2Fredirect'
    #url ='http://1.1.1.1'
    #url = 'http://www.msftconnecttest.com/redirect'
    url = 'https://portaal1.rztienen.be:8443/portal/PortalSetup.action?portal=4f1ab610-d83f-11e8-a0ab-bea55ce933d8'

    with requests.Session() as session:
        response = session.get(url)
        response.text
        html_bytes = response.text
        #soup = bs4(html_bytes, 'lxml')
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

        r_post = session.post(url,data=data)

        pprint(r_post.text)

        with open('index.html','w') as f:
            f.write(response.text)

    #print(get_md5('red'))

# Needed: token, portal, user.username, user.password
# find methods in html code


if __name__ == '__main__':
    main()