from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

# WebDriver চালু করা
driver = webdriver.Chrome()
driver.get("https://www.prothomalo.com/topic/জাহাঙ্গীরনগর-বিশ্ববিদ্যালয়")
time.sleep(3)  # পেজ লোডের জন্য অপেক্ষা

# পেজ সোর্স BeautifulSoup এ পাঠানো
soup = BeautifulSoup(driver.page_source, "html.parser")

# CSV ফাইল তৈরি
with open("jahangirnagar_news.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link"])

    # সমস্ত <a> ট্যাগ পরীক্ষা
    for article in soup.find_all("a", href=True):
        title = article.get_text(strip=True)
        link = article['href']

        # শুধু "জাহাঙ্গীরনগর" শব্দ থাকা লিঙ্ক লিখবে
        if title and "জাহাঙ্গীরনগর" in title:
            if not link.startswith("http"):
                link = "https://www.prothomalo.com" + link
            writer.writerow([title, link])

driver.quit()
print("CSV ফাইল তৈরি হয়েছে: jahangirnagar_news.csv")
