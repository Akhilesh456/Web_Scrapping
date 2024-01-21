from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
DRIVER_PATH = r"C:/SeleniumDrivers" #Change for your computer
SCROLL_PAUSE_TIME = 5
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://crypto.com/nft/marketplace")
last_height = driver.execute_script("return document.body.scrollHeight")
print(last_height)
img_links = []
links = []
for i in range(100):
    driver.execute_script(f"window.scrollTo(0, {last_height})")
    time.sleep(SCROLL_PAUSE_TIME)
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
# while len(img_links) < 10:
doc = BeautifulSoup(driver.page_source,"html.parser")
img_class = "NftCard_nftAssetContainer__6tF6K"
for link in doc.find_all(class_ = img_class):
    try:
        img_links.append(link["style"][23:-3])
    except:
        pass
print(len(img_links))

link_class = "NftCard_linkWrapper__rumHQ"
for link in doc.find_all(class_ = link_class,limit=len(img_links)):
    links.append("https://crypto.com"+link["href"])
print(len(links))


df = pd.DataFrame()
x = min(len(links),len(img_links))
df["Asset Page"] = links[:x]
df["Asset Image"] = img_links[:x]
df.to_csv("nft_data.csv",index=False)
driver.quit()