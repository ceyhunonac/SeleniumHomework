from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
sleep(3)

usernameInput = driver.find_element(By.ID,"user-name")
passwordInput = driver.find_element(By.ID,"password")

class Swag_Test():
    def userNameisEmpty(self):
            usernameInput.send_keys("")
            passwordInput.send_keys("")

            loginButton = driver.find_element(By.ID,"login-button")    
            loginButton.click()  

            nameErrorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
            nameErrorText = nameErrorMessage.text == ("Epic sadface: Username is required")
            print(f"1.{nameErrorText}")

    def passwordisEmpty(self):
            usernameInput.send_keys("asdfg")
            passwordInput.send_keys("")

            loginButton = driver.find_element(By.ID,"login-button")    
            loginButton.click()  

            passwordErrorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
            passwordErrorText = passwordErrorMessage.text == ("Epic sadface: Password is required")
            print(f"2.{passwordErrorText}")

    def senario3(self):
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")

        loginButton = driver.find_element(By.ID,"login-button")    
        loginButton.click() 

        senario3ErrorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        senario3ErrorText = senario3ErrorMessage.text == ("Epic sadface: Sorry, this user has been locked out.")
        print(f"3.{senario3ErrorText}")

    
    def senario4(self):
        usernameInput.send_keys("")
        passwordInput.send_keys("")

        loginButton = driver.find_element(By.ID,"login-button")    
        loginButton.click() 

        sleep(3)

        errorButton = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        errorButton.click()


    def senario5(self):
          
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")

        loginButton = driver.find_element(By.ID,"login-button")    
        loginButton.click() 
        
        driver.get("https://www.saucedemo.com/inventory.html")
    
        numberOfProducts = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Number of products: {len(numberOfProducts)}")
              

            


TestClass = Swag_Test()

TestClass.userNameisEmpty()

TestClass.passwordisEmpty()

TestClass.senario3()

TestClass.senario4()

TestClass.senario5()

    
        

    
    
