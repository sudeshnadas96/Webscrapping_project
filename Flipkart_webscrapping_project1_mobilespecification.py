import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name =[]
Prices=[]
Description=[]
Reviews=[]


for i in range(2,12):
 url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

 r= requests.get(url)
 print(r)
 soup= BeautifulSoup(r.text, "lxml")
 box=soup.find("div", class_ ="_1YokD2 _3Mn1Gg")
 names = box.find_all("div" , class_="_4rR01T")
 print(names)

 for i in names:
    name = i.text
    Product_name.append(name)
    #print(Product_name)
    
 prices = box.find_all("div" , class_ ="_30jeq3 _1_WHN1")
 print(prices)

 for i in prices:
    name= i.text
    Prices.append(name)
 #print(Prices)

 desc= box.find_all("ul", class_="_1xgFaf")
 print(desc)

 for i in desc:
    name = i.text
    Description.append(name)
    
 #print(Description)


 reviews = box.find_all("div", class_="_3LWZlK")
 print(reviews)

 for i in reviews:
   name= i.text
   if (name != None) and (name != ""):
    Reviews.append(name)
   else: Reviews.append("N/A")    
    
 #print(Reviews)
df = pd.DataFrame({"Product name" : Product_name, "Prices" : Prices, "Description" : Description, "Reviews" : Reviews})
print(df)

#df.to_csv("C:/Users/dassu/OneDrive/Documents/flipkart_mobiles_under_50000")



















 #print(soup)
 #while True:
 #np=soup.find("a", class_ = "_1LKTO3").get("href")
 #cnp = "https://www.flipkart.com"+np
 #print(cnp)

 #url=cnp
 #r= requests.get(url)
 #soup= BeautifulSoup(r.text, "lxml")