from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
url = "https://www.google.com"
time.sleep(5)
driver.get(url)

input = driver.find_element(By.NAME, "q")

input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME, "btnK")
time.sleep(2)
searchButton.click()
time.sleep(2)
firstResult=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a")
time.sleep(2)
firstResult.click()
listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f" Listede {len(listOfCourses)} Adet Eğitim vardır.")


#/html/body/section/div/div/div[2]/div[1]/form/div[4]/div/button
#/html/body/section/div/div/div[2]/div[1]/form/div[4]/div/button
#/html/body/section/div/div/div[2]/div[1]/form/div[4]/div/button


# print(f"input :{input}"
#//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a

while True:
    continue
# html locator
