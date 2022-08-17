import requests


def get_info_by_ip(ip):
    print("INFO ABOUT IP:")
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        data = {
            '[IP]': response.get('query'),
            '[PROVAIDER]': response.get('isp'),
            '[ORGANISATION]': response.get('orgy'),
            '[COUNTRY]': response.get('country'),
            '[REGION]': response.get('regionName'),
            '[CITY]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[LAT]': response.get('lat'),
            '[LON]': response.get('lon')
        }
        for k, v in data.items():
            print(f"{k}: {v}")
    except requests.exceptions.ConnectionError:
        print("[!] Connection error")