from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
for laptoplist in range(32):
    if(laptoplist==1):
        page_url = "https://www.startech.com.bd/laptop-notebook/laptop?page="+str(laptoplist)

        print(page_url)

    # opens the connection and downloads html page from url
        uClient = uReq(page_url)

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()

    # finds each product from the store page
        containers = page_soup.findAll("div", {"class": "col-xs-12 col-md-4 product-layout grid"})

    # name the output file to write to local disk
        out_filename = " stertech_laptoplist.csv"
    # header of csv file to be written
        headers = "product_name,product_thumb,price \n"

    # opens file, and writes headers
        f = open(out_filename, "w")
        f.write(headers)

    # loops over each product and grabs attributes about
    # each product
        i = 0
        for container in containers:



            #print(len(container))
            if(i==0):
                #get product thumb
                product_thumb_box = container.find("div", {"class": "product-thumb"})
                product_img_link=product_thumb_box.find('img')['src']
                #get product name
                product_info_box = container.find("div", {"class": "product-info"})
                product_name = product_info_box.find('a').contents[0]
                #get_product_price
                product_price=product_info_box.find('span').contents[0]

                #get_decs
                for tag in product_info_box.findAll("li"):
                    print("{0}: {1}".format(tag.name, tag.text))


               # print(product_price)





        f.close()


        # Grabs the title from the image title attribute
        # Then does proper casing using .title()
        #brand = make_rating_sp[0].img["title"].title()

        # Grabs the text within the second "(a)" tag from within
        # the list of queries.
       # product_name = container.div.select("a")[2].text

        # Grabs the product shipping information by searching
        # all lists with the class "price-ship".
        # Then cleans the text of white space with strip()
        # Cleans the strip of "Shipping $" if it exists to just get number
       # shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

        # prints the dataset to console
        #print("brand: " + brand + "\n")
       # print("product_name: " + product_name + "\n")
       # print("shipping: " + shipping + "\n")

        # writes the dataset to file
        #f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")


