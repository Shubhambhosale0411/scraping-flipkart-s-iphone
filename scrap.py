from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

uclient=uReq(url)
page_html=uclient.read()
uclient.close()
page_soup=soup(page_html,"html.parser")

container=page_soup.findAll("div",{"class":"_13oc-S"})
#print(len(container))    #no.of products
#print(soup.prettify(container[0]))   #html code for first container
containers=container[0]

#print(container.div.img["alt"])


#main game begins   from here  apple bro
title=containers.findAll("div",{"class":"_4rR01T"}) 


#price=containers.findAll("div",{"class":"col col-5-12 nlI3QM"})


price=containers.findAll("div",{"class":"_3I9_wc _27UcVY"})   
# --imp
#print(price[0].text)



rating=containers.findAll("span",{"class":"_2_R_DZ"})
#print(rating[0].text)

filename="products.csv"
f=open(filename,"w")

headers="productname,pricing,rating\n"
f.write(headers)

for containers in container:
    product_name=containers.findAll("div",{"class":"_4rR01T"})
    product=product_name[0].text
    price_container=containers.findAll("div",{"class":"_3I9_wc _27UcVY"})
    price=price_container[0].text.strip()

    rating_container=containers.findAll("span",{"class":"_2_R_DZ"})
    rating=rating_container[0].text

    #print("product_name: "+product)
    #print("price: "+price)
    #print("rating: "+rating)

    #can add trim

    f.write(product +","+price+","+rating+"\n")
f.close()


