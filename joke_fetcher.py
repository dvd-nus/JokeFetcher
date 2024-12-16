# joke_fetcher.py
import httpx

async def fetch_jokes(num_jokes=100):
    url = "https://v2.jokeapi.dev/joke/Any"
    jokes = []
    
    async with httpx.AsyncClient() as client:
        while len(jokes) < num_jokes:
            # Dynamically adjust the amount of jokes per request
            amount = min(num_jokes - len(jokes), 10)  # Fetch up to 10 jokes, or the remaining count if less than 10

            response = await client.get(url, params={"lang": "en", "safe-mode": "true", "amount": amount})
            data = response.json()  # Await the response and parse it
            
            # Check if the response contains jokes
            if "jokes" in data:  # Ensure we have the jokes key in the response
                for joke_data in data["jokes"]:
                    # Process single joke type
                    if joke_data["type"] == "single":
                        joke = {
                            "category": joke_data["category"],
                            "joke_type": "single",
                            "joke": joke_data["joke"],
                            "setup": None,
                            "delivery": None,
                            "nsfw": joke_data.get("flags", {}).get("nsfw", False),
                            "political": joke_data.get("flags", {}).get("political", False),
                            "sexist": joke_data.get("flags", {}).get("sexist", False),
                            "safe": joke_data.get("flags", {}).get("safe", True),
                            "lang": joke_data["lang"]
                        }
                    # Process two-part joke type
                    elif joke_data["type"] == "twopart":
                        joke = {
                            "category": joke_data["category"],
                            "joke_type": "twopart",
                            "joke": None,
                            "setup": joke_data["setup"],
                            "delivery": joke_data["delivery"],
                            "nsfw": joke_data.get("flags", {}).get("nsfw", False),
                            "political": joke_data.get("flags", {}).get("political", False),
                            "sexist": joke_data.get("flags", {}).get("sexist", False),
                            "safe": joke_data.get("flags", {}).get("safe", True),
                            "lang": joke_data["lang"]
                        }
                    
                    # Add the processed joke to the jokes list
                    jokes.append(joke)
    
    # Return only the required number of jokes (in case we fetched more)
    return jokes
