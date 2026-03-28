import requests
import json
import re

def fetch_channels():
    # यहाँ उस साइट का API या सोर्स लिंक डालें जहाँ से डेटा आ रहा है
    # उदाहरण के लिए हम एक डमी स्ट्रक्चर ले रहे हैं
    target_url = "https://raw.githubusercontent.com/Shubhamkur/Tv/refs/heads/main/tvid"
    
    try:
        response = requests.get(target_url)
        if response.status_code == 200:
            data = response.json()
            
            # यहाँ आप अपना फ़िल्टर लगा सकते हैं (जैसे सिर्फ Sports या Ent)
            # अभी के लिए हम पूरा डेटा ले रहे हैं
            with open("tvid.json", "w") as f:
                json.dump(data, f, indent=4)
            print("Channels updated successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_channels()
