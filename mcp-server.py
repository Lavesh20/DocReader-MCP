# step 1 : lets create a function which uses the serper api to search for a query
# and return the results

import os
import requests
from dotenv import load_dotenv

load_dotenv()

url  = "https://google.serper.dev/search"

def search_serper(query: str) -> dict:
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError("SERPER_API_KEY is not set.")

    

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
    }

    payload = {
        "q": query,
        "num": 2
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    results = search_serper("ChromaDB")
    print(results)
