#web scraping program for basmati rice offer prices at morrisons

import requests
from bs4 import BeautifulSoup 

def main():
    morrisons()
    
  


def morrisons():
    morrisons_b_rice = requests.get("https://groceries.morrisons.com/categories/food-cupboard/rice-pasta-noodles-pulses/rice/basmati-rice/c6a685e7-fc9c-4cbb-b654-6f47832ee1e0?boolean=onOffer&sortBy=favorite")
    soup = BeautifulSoup(morrisons_b_rice.text, "html.parser")
    products = soup.find_all("h3", attrs={"class": "_text_cn5lb_1 _text--m_cn5lb_23" })
    weights = soup.find_all("span", attrs={"class": "_text_cn5lb_1 _text--m_cn5lb_23 _weight_18pzb_1"})
    prices = soup.find_all("span", attrs={"class":"_display_xy0eg_1 sc-1fkdssq-1 eDGgtR"})


    for product, weight, price in zip(products, weights, prices):
       print(product.text,""+"",  weight.text,""+"", price.text)


     
   
    

if __name__ == "__main__":
    main()
