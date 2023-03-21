from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from webdriver_manager.chrome import ChromeDriverManager


class TestKodlamaio:
    def test_invalid_login(self):
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome()
        url = "https://www.saucedemo.com"
        driver.get(url)
        time.sleep(2)
        # "standard_user"
        userNames = ["standard_user","" , "locked_out_user",
                     "problem_user", "performance_glitch_user", "user_name"]
        password = [".","secret_sauce"]

        for user in userNames:

            username = driver.find_element(By.NAME, "user-name")
            username.send_keys(user)
           
            time.sleep(1)
            for password in password:

                sifrealani = driver.find_element(By.NAME, "password")
                sifrealani.send_keys(password)
                time.sleep(1)

                loginBtn = driver.find_element(By.NAME, "login-button")
                loginBtn.click()
                error=driver.find_element(By.CLASS_NAME,"")
                
                
                time.sleep(4)
                
        print("Seçildi")
            
            # error=driver.find_element(By.CLASS_NAME,"")
            
        


testClass = TestKodlamaio()

testClass.test_invalid_login()
