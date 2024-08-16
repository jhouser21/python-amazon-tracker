import requests
from bs4 import BeautifulSoup
import lxml
import pprint
HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=HEADERS)


soup = BeautifulSoup(response.text, "html.parser")

spansPriceWhole = soup.select('span.a-price-whole')
spansPriceFraction = soup.select('span.a-price-fraction')

pricesFraction = [pricef.get_text().strip(".") for pricef in spansPriceWhole]
pricesWhole = [pricew.get_text() for pricew in spansPriceWhole]

totalPrice = pricesWhole[0] + pricesFraction[0]
print(float(totalPrice))