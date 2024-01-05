import requests, re
ses = requests.Session()

uid = input(" masukan uid : ")
pw = input(" masukan pw : ")
link = ses.get("https://mobile.prod.facebook.com/login/device-based/password/?uid="+uid+"flow=login_no_pin&skip_api_login=1&next=https%3A%2F%2Fmobile.prod.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D8744a0ccdce1491c4474dacf75dc2d12%26redirect_uri%3Dhttp%253A%252F%252Fwww.myspace.com%252Ffbocallback%253Fuhp%253Duhp%26scope%3Demail%252Coffline_access%252Cuser_about_me%252Cuser_birthday%252Cuser_likes%252Cpublish_stream%252Cpublish_actions%26display%3Dpopup%26from_login%3D1&cancel_uri=http%3A%2F%2Fwww.myspace.com%2Ffbocallback%3Fuhp%3Duhp&display=popup&api_key=8744a0ccdce1491c4474dacf75dc2d12")
dta = {
    "lsd": re.search('"lsd" value="(.*?)"',str(link.text)).group(1),
    "jazoest": re.search('"jazoest" value="(.*?)"',str(link.text)).group(1),
    "uid": uid,
    "next": "",
    "flow": "login_no_pin",
    "pass": pw }

hd = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Alt-Used": "mobile.prod.facebook.com",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "mobile.prod.facebook.com",
    "Origin": "https://mobile.prod.facebook.com",
    "Referer": "https://mobile.prod.facebook.com/login/device-based/password/?uid=100076851501718&flow=login_no_pin&skip_api_login=1&next=https%3A%2F%2Fmobile.prod.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D8744a0ccdce1491c4474dacf75dc2d12%26redirect_uri%3Dhttp%253A%252F%252Fwww.myspace.com%252Ffbocallback%253Fuhp%253Duhp%26scope%3Demail%252Coffline_access%252Cuser_about_me%252Cuser_birthday%252Cuser_likes%252Cpublish_stream%252Cpublish_actions%26display%3Dpopup%26from_login%3D1&cancel_uri=http%3A%2F%2Fwww.myspace.com%2Ffbocallback%3Fuhp%3Duhp&display=popup&api_key=8744a0ccdce1491c4474dacf75dc2d12",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"}

post = ses.post(f"https://mobile.prod.facebook.com/login/device-based/validate-password/?shbl=0",data=dta, headers=hd,allow_redirects=False)
print(ses.cookies.get_dict())
