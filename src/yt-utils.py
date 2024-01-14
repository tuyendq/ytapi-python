import requests
import re

url = 'https://www.youtube.com/@annenguyen7979'
url_invalid = 'https://www.youtube.com/@annenguyen79'

def get_channel_id(channel_url):
    """Find channel id from channel url"""

    x = requests.get(channel_url)
    pattern = 'https://www\.youtube\.com/channel/([^\s"]+)'

    if x.status_code==200:
        txt = x.text
        match = re.search(pattern, txt)
        if match:
            # print(match)
            # print(match.span())
            # print(match.group(0))
            # print(match.group(1))
            return match.group(1)
        else:
            print("Cannot find channel id!")
    else:
        print(f"Cannot access {url}")
        return None

# Test valid url
print(get_channel_id(url))
# Test invalid url
print(get_channel_id(url_invalid))