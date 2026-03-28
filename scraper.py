import requests
import re

# टारगेट वेबसाइट
TARGET_URL = "https://tvgotk.pages.dev/"

def get_links():
    try:
        # वेबसाइट को ऐसा लगना चाहिए कि कोई असली इंसान Chrome ब्राउज़र से देख रहा है
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }
        
        print("वेबसाइट से डेटा ला रहा हूँ...")
        response = requests.get(TARGET_URL, headers=headers, timeout=30)
        
        # सभी .m3u8 लिंक ढूंढना (चाहे वो छोटे हों या बड़े)
        links = re.findall(r'(https?://[^\s<>"]+?\.m3u8[^\s<>"]*)', response.text)
        
        # अगर .m3u8 नहीं मिले, तो .mpd लिंक ढूंढना
        if not links:
            links = re.findall(r'(https?://[^\s<>"]+?\.mpd[^\s<>"]*)', response.text)

        with open("live_tv.m3u", "w") as f:
            f.write("#EXTM3U\n")
            if not links:
                print("कोई लिंक नहीं मिला!")
                f.write("#EXTINF:-1, [No Links Found - Update Scraper]\nhttp://example.com/check.m3u8\n")
            else:
                print(f"{len(links)} लिंक मिले!")
                for i, link in enumerate(links):
                    # लिंक से नाम निकालने की कोशिश (अगर उपलब्ध हो)
                    f.write(f"#EXTINF:-1, Channel {i+1}\n{link}\n")
                    
        print("फाइल सफलतापूर्वक अपडेट हो गई!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_links()
