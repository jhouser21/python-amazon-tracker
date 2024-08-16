import requests
from bs4 import BeautifulSoup
import lxml

HEADERS = {'User Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
            "Accept-Language": "en-US,en;q=0.9"}

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=HEADERS)

print(response.text)

soup = BeautifulSoup(response.content, "lxml")

# print(soup)