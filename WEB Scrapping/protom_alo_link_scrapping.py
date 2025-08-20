from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

# webdriver চালু করো
driver = webdriver.Chrome()
driver.get("https://www.prothomalo.com/topic/জাহাঙ্গীরনগর-বিশ্ববিদ্যালয়")
time.sleep(3)  # পেজ লোড হওয়ার সময় দিন

# পেজ সোর্স নিয়ে BeautifulSoup এ পাঠানো
soup = BeautifulSoup(driver.page_source, "html.parser")

# CSV ফাইল খোলা (লেখার জন্য)
with open("prothomalo_links.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link"])  # হেডার লিখে দেওয়া

    # সব <a> ট্যাগ থেকে টেক্সট আর লিঙ্ক নেওয়া
    for article in soup.find_all("a", href=True):
        title = article.get_text(strip=True)
        link = article['href']
        writer.writerow([title, link])  # CSV তে লিখে দেওয়া

driver.quit()
