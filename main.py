from bs4 import BeautifulSoup
import lxml
import smtplib
import requests

USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
ACCEPT_LANGUAGE="en-US,en;q=0.9"
url="https://www.amazon.in/Anker-4-Port-Ultra-Extended-MacBook/dp/B07L32B9C2/ref=sr_1_3?crid=36K84P47C3GZ0&keywords=anker+usb+hub&qid=1647951499&sprefix=anker+usb+hub%2Caps%2C233&sr=8-3"

MY_EMAIL = "raghupythontest@gmail.com"
MY_PASSWORD = "Raghu1234"

headers = { 'Accept-Language':USER_AGENT,
            'User-Agent':ACCEPT_LANGUAGE
          }
response=requests.get(url=url,headers=headers)
amazon_web=response.text
soup=BeautifulSoup(amazon_web,"lxml")

price=soup.find(name="span",class_="a-price-whole").getText()
print(price)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"The price got decreased to {price} go ahead and buy now"
    )
