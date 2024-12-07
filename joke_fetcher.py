# joke_fetcher.py
import requests

def fetch_jokes(num_jokes=100):
    url = "https://v2.jokeapi.dev/joke/Any"
    jokes = []
    
    while len(jokes) < num_jokes:
        response = requests.get(url, params={"lang": "en", "safe-mode": "true"})
        data = response.json()
        
        if data["type"] == "single":
            joke = {
                "category": data["category"],
                "joke_type": "single",
                "joke": data["joke"],
                "setup": None,
                "delivery": None,
                "nsfw": data.get("flags", {}).get("nsfw", False),
                "political": data.get("flags", {}).get("political", False),
                "sexist": data.get("flags", {}).get("sexist", False),
                "safe": data.get("flags", {}).get("safe", True),
                "lang": data["lang"]
            }
        elif data["type"] == "twopart":
            joke = {
                "category": data["category"],
                "joke_type": "twopart",
                "joke": None,
                "setup": data["setup"],
                "delivery": data["delivery"],
                "nsfw": data.get("flags", {}).get("nsfw", False),
                "political": data.get("flags", {}).get("political", False),
                "sexist": data.get("flags", {}).get("sexist", False),
                "safe": data.get("flags", {}).get("safe", True),
                "lang": data["lang"]
            }
        
        jokes.append(joke)
    
    return jokes
