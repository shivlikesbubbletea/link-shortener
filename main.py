# API(s) used: Bitly, Shortest, Cuttly


import bitly_api
import time 
import json 
import pyshorteners
import urllib
import requests

print("Welcome to link shortener")
options = '''
1) Bitly 
2) Pyshorteners
3) Cuttly

Please note that some API(s) might not work due to rate limits
'''
print(options)
used_api = input("Please choose the preferred API: ")

if used_api == '1' or 'Bitly':
    try: 
        token = 'e9d12cec75170768ba02120a22229bc08ede86cb'
        
        connection = bitly_api.Connection(access_token=token)
        url = input('Enter URL: ')
        short_url= connection.shorten(url)
        data = json.dumps(short_url)
        jdata = json.loads(data)
        jdata = jdata['url']
        print('Short URL: ',jdata)
    except:
        print('An error occurred')
        time.sleep(2)
        exit()
elif used_api == '2' or 'Pyshorteners':
    try:
        url = input('Enter URL: ')
        shortener = pyshorteners.Shortener()
        print('Short URL: ',shortener.tinyurl.short(url))

    except:
        print('An error occurred')
        time.sleep(2)
        exit()
elif used_api == '3' or 'Cuttly':
    try: 
        key = '6e7bbfad6cd410eff77a65fbb6b27fbbffef3'
        url = urllib.parse.quote(input('URL to shorten'))
        name  = input('Name of link: ')
        r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
        print('Short URL: ',r.text)
    except:
        print('An error occurred')
        time.sleep(2)
        exit()