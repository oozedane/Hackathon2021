import pandas as pd
import requests
from bs4 import BeautifulSoup

bottin =[]
for i in range(59):
    url = "https://www.cpascharleroi.be/fr/bottin-social-recherche?title=&commune=All&page=0"
    true_url = url+str(i)
    print(true_url)
    req = requests.get(true_url)
    soup = BeautifulSoup(req.text, "lxml")
    mydivs = soup.findAll("div", {"class": "views-field views-field-title"})
    data = soup.find_all("a",{'class':'result-link'})
    type(data)
    list = []
    for a in data:
        print(type(a))
        for line in a :
            list.append(line)
            bottin.append(line)
data_bottin = pd.DataFrame(bottin)

categorie = ["Emploi"]
draw_url = "https://www.cpascharleroi.be/fr/bottin-social/"
url_with_category = draw_url+"agences-locales-pour-l-emploi"+"/"
url_total= url_with_category+"agence-locale-pour-l-emploi-d-aiseau-presles"+"?destination=bottin-social"
print(url_total)
req2 = requests.get(url_total)
soup2 = BeautifulSoup(req2.text, "lxml")
mydivs2 = soup2.findAll("div", {"class":'organism-field'})
type(mydivs2)

print(mydivs2[2])
test=[]
for i in mydivs2[2] :
    for d in i :
        if isinstance(d,str):
            print("hello")
        else:
            d=str(d)
            test.append(d)

print([s.strip('<div>') for s in test])


## GERMAIN
import pandas as pd
import requests
from bs4 import BeautifulSoup

bottin =[]
categories=[]
for i in range(2):
    url = "https://www.cpascharleroi.be/fr/bottin-social-recherche?title=&commune=All&page=0"
    true_url = url+str(i)
    print(true_url)
    req = requests.get(true_url)
    soup = BeautifulSoup(req.text, "lxml")
    mydivs = soup.findAll("div", {"class": "views-field views-field-title"})
    myhref= soup.findAll("a",{"class":"result-link"})
    for a in myhref:
        href = a['href']
        url_pages= "https://www.cpascharleroi.be"+str(href)
        href= str(href)
        categorie = href.split("bottin-social/",1)[1]
        categorie= categorie.split("/")[0]
        categorie=categorie.replace("-"," ")
        print(categorie)
        categories.append(categorie)
        req3 = requests.get(url_pages)
        soup3 = BeautifulSoup(req3.text, "lxml")
        data = soup.find_all("a",{'class':'result-link'})
        list = []
        for a in data:
            print(type(a))
            for line in a :
                list.append(line)
                bottin.append(line)
        data_bottin = pd.DataFrame(bottin)


import numpy as np
bottin_social=pd.DataFrame({"Association" : bottin,"Categorie":categories})


##END GERMAIN

test = requests.get("https://www.cpascharleroi.be/fr/bottin-social/enfance-et-jeunesse/les-petits-spirou-service-d-aide-et-d-intervention-educative?destination=bottin-social")
print(type(test))

soup_test= BeautifulSoup(test.text,'lxml')
mydivs_text= soup_test.findAll("div",{"class":"content"},)
d=[]
for price in soup_test.findAll("div", {"class": "content"}): d.append(price.get_text(separator="\n ",strip=True))

from bs4 import Tag, NavigableString, BeautifulSoup


info =(mydivs_text[3].contents)

list_info= []
for i in info :
    if isinstance(i,Tag):
        print(type(i))
        list_info.append(str(i))
    else:
        print("0")
convert_list=[]
for element in list_info:
    if element =="\\n " or element =="<br/":
        list_info.pop(element)
    else :
        convert_list.append(element)
raw = str(convert_list)

def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
print(type(info))
print(info[0])
for i in str(info) :
    print(remove_html_tags(i))
    print(i)


test_arturito= remove_html_tags(str(info))
list_test_arturito= list(test_arturito)
print(type(list_test_arturito))
print(list_test_arturito[0])
for element in list_test_arturito :
    print(element)
new_string = " ".join(test_arturito.splitlines())
test_arturito2=test_arturito.replace("\n","")
for element in test_arturito :
    print(element.strip())

dr=remove_html_tags(raw)
dmd= dr.rstrip()
a=dmd.split(",")
m=[]
for i in a :
    i.replace("\\n"," ")
    m.append(i)
    print(i)


my_string="hello python world , i'm a beginner "
print (my_string.split("world",1)[1] )
