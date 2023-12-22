from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
import os
import constants

os.environ["GOOGLE_CSE_ID"] = constants.GOOGLEID
os.environ["GOOGLE_API_KEY"] = constants.GAPIKEY


search = GoogleSearchAPIWrapper(k=1)

def top5_results(query):
    return search.results(query,2)

def googleSearch(searc):
    tool = Tool(name="I'm feeling Lucky", description="Search Google and return the first result.", func=top5_results)

    result = tool.run(searc)

    return result
googlesearch=googleSearch(searc=input("Enter a search: "))
print(googlesearch)

for i in googlesearch:
    for key, value in i.items():
        print(f"{key} : {value}")
