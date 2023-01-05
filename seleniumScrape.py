from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/chromedriver.exe")
result = driver.get("https://www.youtube.com/results?search_query=cats")

videoTitles = driver.find_elements(By.ID, "video-title")

for videoTitle in videoTitles:
    print(videoTitle.text)

