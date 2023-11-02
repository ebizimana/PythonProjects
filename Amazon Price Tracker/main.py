import requests
import smtplib
from bs4 import BeautifulSoup


my_email = "elieb7842@gmail.com"
password = "dwsovuqytspgbrlo"

url = "https://www.amazon.com/dp/B09327SCLJ/ref=fs_a_ipadt2_us0?th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/15.4 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9"}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

price_tag = soup.find(name="span", class_="a-price-whole")
product_title_tag = soup.find(name="span", id="productTitle")
product_title = product_title_tag.getText().strip()
price = price_tag.getText().split(",")
price = float("".join(price))

if price <= 1000.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Amazon Price Alert!\n\n{product_title.encode('utf-8')} is now ${price}\n{url}")


