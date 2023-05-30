import requests
from bs4 import BeautifulSoup

query=input("Enter input query: ")
response=requests.get("https://www.amazon.in/s?k={}".format(query))
soup=BeautifulSoup(response.text,"lxml")
item_divs=soup.findAll('div',attrs={"data-component-type":"s-search-result"})
try:
    for (index,each_item) in enumerate(item_divs):
        print(str(index+1)+"->"+each_item.findChild('div').findChild('div').findChild('div').findChild('div').findChild('div').findChildren('div',recursive=False)[1].find('span').contents[0],"\n")
except:
    print("Need to work on this type of results :(")