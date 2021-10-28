#importing beautiful soup and requests modules
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

url = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_1_sspa?crid=2J7Z2H4JU9MYE&dchild=1&keywords=macbook+air&qid=1635317913&sprefix=macbook%2Caps%2C353&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNjZMOUVOU0wwOE00JmVuY3J5cHRlZElkPUExMDQxMjcwMU5DV1JFTFhQS1g0TyZlbmNyeXB0ZWRBZElkPUEwNzA2OTgyM00zSFVJMlJEOTFTSiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,"html.parser")

def check_price():
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").text
    print("product name : ", title)
    print("product price : ", price)


smtp_server = "smtp.gmail.com"
port = 587
email_id1 = "chvinayaka19@gmail.com"
password = "iprrlmjexwptolzj"
email_id2 = "vinayakach21@gmail.com"

server = SMTP(smtp_server, port)
server.starttls()
server.login(email_id1, password)

subject = "hey, buy now!"
body = "price has fallen\n go and buy it now from this link " + url
msg = f"subject : {subject}\n\n{body}"

server.sendmail(email_id1,email_id2,msg)
server.quit()

check_price()
