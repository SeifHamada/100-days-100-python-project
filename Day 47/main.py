from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
BUY = 50

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.amazon.com/",
    "DNT": "1",
    "Connection": "keep-alive"
}
response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
price = float(soup.find(class_="a-price-whole").get_text())
# plain_price = float(price.split("$")[1])
# print(price)

title = soup.find(id="productTitle").get_text().strip()
# print(title)

if price < BUY:
    message = f"Buy {title} quick before the sale ends for {price}."

    with smtplib.SMTP("example@gmail.com", port=587) as connection:
        connection.starttls()
        connection.login("example@gmail.com", "Password123")
        connection.sendmail(
            from_addr="example@gmail.com",
            to_addrs="example@gmail.com",
            msg="The item you were looking for is on sale right now buy it before the sale ends.\n\n{message}\n{url}".encode(
                "utf-8")
        )
