import requests,re
ses = requests.Session()
url = 'm.facebook.com'
user = input(' masukan id : ')
pw = input(' masukan pw : ')
wibu = ses.get(f'https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&hbl=0&refsrc=deprecated').text
data = {
  "lsd": re.search('name="lsd" value="(.*?)"',str(wibu)).group(1),
  "jazoest": re.search('name="jazoest" value="(.*?)"', str(wibu)).group(1),
  "uid": user,
  "next": f"https://{url}/login/save-device/",
  "flow": "login_no_pin",
  "pass": pw
       }
wibu_head = {
  'Host': url,
	'cache-control': 'max-age=0',		
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'upgrade-insecure-requests': '1',
	'origin': url,
	'content-type': 'application/x-www-form-urlencoded',
  'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-user': '?1',
	'sec-fetch-dest': 'document',
	'referer': f'https://{url}/login/device-based/password/?uid={user}&flow=login_no_pin&hbl=0&refsrc=deprecated',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
post = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0",data=data,headers=wibu_head,allow_redirects=False)
print(ses.cookies.get_dict())

  
