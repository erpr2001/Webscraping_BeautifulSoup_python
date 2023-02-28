import requests
from bs4 import BeautifulSoup
url = "https://....."

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# commonly used types of obj:
# tag: print(type(title))
# navigablestring: print(type(title.string))
# BeautifulSoup: print(type(soup))
# comment:   markup="<p><!--this is a comment--></p>"
#            soup2=BeautifulSoup(markup)
#            print(type(soup2.p.string))
title = soup.title  # get title of html page

paras = soup.find_all('p')
# print(paras)   get all paras

anchors = soup.find_all('a')
# print(anchors)
all_links = set()
for link in anchors:
    if (link != '#'):
        linkText="https://codewithharry.com"+link.get('href')
        all_links.add(linkText)
        print(linkText)

# print(soup.find('p'))    gives first paragraph of html pg
# print(soup.find('p')['class'])  gives class of html page
# print(soup.find('p')['id'])  gives key error because id is not present

# print(soup.find_all("p",class_="lead")) #find element with class lead
# print(soup.find("p").get_text()) # get text from tags/soup
# print(soup.get_text())

navbarSupportedContent=soup.find(id="navbarSupportedContent")
# print(navbarSupportedContent.children)
# print(navbarSupportedContent.contents)
# .contents- a tag's children r available as list.- memory ma stored
# .children- a tag's children r available as item/generator. -not stored in memory but can be prapt by iteration or using some next function. 
# for elem in navbarSupportedContent.contents: # both give same o/p #for elem in navbarSupportedContent.children:    
#     # print(elem)
# for itm in navbarSupportedContent.parents:
#     print(itm)

# print(navbarSupportedContent.next_sibling.next_sibling) #etle nxt sibling ni pan nxt sibling
# print(navbarSupportedContent.previous_sibling.previous_sibling)


# elem=soup.select('#loginModal') # '#'-gives elment loginmodal's id & if "."-will give class
# print(elem) 
elem=soup.select('.modal-footer')
print(elem)

