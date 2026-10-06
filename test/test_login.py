from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(
        EC.url_contains("/inventory.html")
    )
    assert "/inventory.html" in driver.current_url
    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo.text == "Products"
    driver.quit()