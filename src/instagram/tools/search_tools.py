import requests
import json
import os
from langchain_core.tools import tool
from langchain_community.document_loaders import WebBaseLoader

class SearchTools:
    @tool('search internet')
    def search_internet(query: str) -> str:
        """
        Use this tool to search the internet for information. This tool returns 5 results from Google Search Engine.
        """
        return SearchTools.search(query)
    
    @tool('search instagram')
    def search_instagram(query: str) -> str:
        """
        Use this tool to search instagram. This tool returns 5 results from instagram pages.
        """
        return SearchTools.search(f"site:instagram.com {query}")
    
    @tool('open webpage')
    def open_webpage(url: str) -> str:
        """
        Use this tool to open a webpage and get the content.
        """
        loader = WebBaseLoader(url)
        return loader.load()


    def search(query, limit=5):
        url = "https://google.serper.dev/search"

        payload = json.dumps({
        "q": query,
        "num": limit
        })

        headers = {
        'X-API-KEY': os.environ["SERPER_API_KEY"],
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).json()

        final_results = []
        for element in response["organic"]:
            final_results.append(
                f"{element['title']}\n{element['link']}\n{element['snippet']}"
            )
        return f"Search results for '{query}':\n\n" + "\n".join(final_results)
    