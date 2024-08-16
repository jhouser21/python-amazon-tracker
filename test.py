import requests
from bs4 import BeautifulSoup
import lxml


HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=HEADERS)


# soup = BeautifulSoup(response.text, "html.parser")
# # print(soup)
#
# price_pull = soup.select("span.a-price-whole")
# tru_price = [price.getText().strip(".") for price in price_pull]

# print(price_pull)

soup = BeautifulSoup(response.text, "html.parser")

spansPriceWhole = soup.find(name="span", class_="a-price-whole")
spansCents = soup.find(name="span", class_="a-price-fraction")

print(f"The product is currently ${spansPriceWhole.get_text().split()[0]}{spansPriceWhole.get_text().split()[0]}")

# soup = BeautifulSoup(response.text, "html.parser")
#
# spansPriceWhole = soup.select('span.a-price-whole')
#
# prices = [price.get_text().strip(".") for price in spansPriceWhole]
#
# print(prices)