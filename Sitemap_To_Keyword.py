import requests
from lxml import etree

def Crawl_Website():
    xmlList = []

    website_URl = "https://gamingspice.com/"
    r = requests.get(website_URl+"post-sitemap.xml")
    root = etree.fromstring(r.content)
    for sitemap in root:
        children = sitemap.getchildren()
        xmlList.append(children[0].text)
        
    for url in xmlList:
        s = url.replace("-", " ")
        s = s.replace(website_URl, "")
        s = s.replace("/", "").title()
        f = open("keywords.txt", "a")
        f.write(s+"\n")
        f.close()
        print(s)


Crawl_Website()

