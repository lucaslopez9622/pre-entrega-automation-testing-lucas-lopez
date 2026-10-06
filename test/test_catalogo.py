from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.help import iniciar_sesion


def test_catalogo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    iniciar_sesion(driver)

    wait = WebDriverWait(driver, 10)

    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert titulo.text == "Products"

    productos = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    assert len(productos) > 0

    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")

    menu = driver.find_element(
        By.ID, "react-burger-menu-btn"
    )

    assert menu.is_displayed()

    filtro = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )

    assert filtro.is_displayed()

    driver.quit()