from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class TestCase_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Result : {testResult}")

    def test_null_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Result : {testResult}")

    def test_locked_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Result : {testResult}")

    def test_error_icon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorIcon = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(2)
        errorIcon.click()

    def test_login_inventory(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        driver.current_url == ("https://www.saucedemo.com/inventory.html")
        sleep(2)

    def test_all_product(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        lenProduct = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Lenght Product Result : {len(lenProduct)}")
        while True:
            continue


sauceTest = TestCase_Sauce()
sauceTest.test_all_product()




