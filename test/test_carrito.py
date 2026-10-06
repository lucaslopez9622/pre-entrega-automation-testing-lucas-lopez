from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.help import iniciar_sesion

def test_carrito():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    iniciar_sesion(driver)
    wait = WebDriverWait(driver, 10)
    primer_producto = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    nombre_producto = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    boton_agregar = primer_producto.find_element(
        By.TAG_NAME, "button"
    )

    boton_agregar.click()
    contador = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert contador.text == "1"
    carrito = driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    )

    carrito.click()
    wait.until(
        EC.url_contains("/cart.html")
    )

    producto_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert producto_carrito.text == nombre_producto
    driver.quit()
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

    primer_producto = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    nombre_producto = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    boton_agregar = primer_producto.find_element(
        By.TAG_NAME, "button"
    )

    boton_agregar.click()

    contador = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert contador.text == "1"

    carrito = driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    )

    carrito.click()

    wait.until(
        EC.url_contains("/cart.html")
    )

    producto_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert producto_carrito.text == nombre_producto

    driver.quit()