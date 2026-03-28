import requests
import re

TARGET_URL = "https://tvgotk.pages.dev/"

def get_links():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }
        response = requests.get(TARGET_URL, headers=headers, timeout=20)
        
        # .m3u8 वाले लिंक ढूंढना
        links = re.findall(r'(https?://[^\s<>"]+\.m3u8)', response.text)
        
        with open("live_tv.m3u", "w") as f:
            f.write("#EXTM3U\n")
            if not links:
                f.write("#EXTINF:-1, No Links Found\nhttp://example.com/check.m3u8\n")
            else:
                for i, link in enumerate(links):
                    f.write(f"#EXTINF:-1, Live Channel {i+1}\n{link}\n")
        print(f"Done! {len(links)} links found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_links()
