import requests
import re

# जिस साइट से डेटा फेच करना है
TARGET_URL = "https://tvgotk.pages.dev/"

def get_links():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(TARGET_URL, headers=headers)
        
        # .m3u8 वाले लिंक ढूंढना
        links = re.findall(r'https?://[^\s<>"]+\.m3u8', response.text)
        
        # M3U फाइल बनाना
        with open("live_tv.m3u", "w") as f:
            f.write("#EXTM3U\n")
            for i, link in enumerate(links):
                f.write(f"#EXTINF:-1, Live Channel {i+1}\n{link}\n")
        print("Done!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_links()
