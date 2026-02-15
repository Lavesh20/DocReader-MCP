# step 1 : lets create a function which uses the serper api to search for a query
# and return the results

import os
import httpx
from dotenv import load_dotenv
import asyncio


load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY is not set.")

SERPER_URL = "https://google.serper.dev/search"


async def search_serper(query: str) -> dict:
    payload = {
        "q": query,
        "num": 2
    }

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post(
            SERPER_URL,
            json=payload,
            headers=headers
        )

        response.raise_for_status()
        return response.json()



if __name__ == "__main__":
    async def main():
        results = await search_serper("Langchain")
        print(results)

    asyncio.run(main())