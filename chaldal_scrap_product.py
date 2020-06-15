from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
for laptoplist in range(32):
    if(laptoplist==1):
        page_url = "https://chaldal.com/rice-2"

        print(page_url)

    # opens the connection and downloads html page from url
        uClient = uReq(page_url)

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()

    # finds each product from the store page
        containers = page_soup.findAll("div", {"class": "product"})

    # name the output file to write to local disk
        out_filename = " chaldal_rice_list.csv"
    # header of csv file to be written
        headers = "product_name,image,quantity,price \n"

    # opens file, and writes headers
        f = open(out_filename, "w", encoding='utf-8')
        f.write(headers)

        for container in containers:
             product_box2 = container.find("div", {"class": "imageWrapper"})
             #product name
             product_name= product_box2.find("div", {"class": "name"})
             print(product_name.text)
             #product price
             product_price= product_box2.find("div", {"class": "price"})
             price
             print(product_price.text)
             #produt quantity
             product_qun= product_box2.find("div", {"class": "subText"})
             print(product_qun.text)
             #produt thumbnail
             product_thumb= product_box2.find('img')['src']
             print(product_thumb.strip())

             f.write(product_name.text + ',' + product_thumb+','+ product_qun.text +','  + product_price.text + '\n')
        f.close()




