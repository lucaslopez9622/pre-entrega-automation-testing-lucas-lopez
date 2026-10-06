Proyecto de automatización de pruebas sobre SauceDemo utilizando Selenium WebDriver y Pytest.

proposito del proyecto
Automatizar pruebas funcionales sobre SauceDemo para verificar el correcto funcionamiento del inicio de sesión, catálogo de productos y carrito de compras, utilizando Selenium WebDriver y Pytest.


Tecnologías utilizadas
-Python
-Selenium WebDriver
-Pytest
-Pytest HTML


Instalación
Crear y activar un entorno virtual:
python -m venv venv
venv\Scripts\activate

Instalar las dependencias:
pip install -r requirements.txt



Ejecutar las pruebas

Para ejecutar todos los tests:
pytest -v

Para generar el reporte HTML:
pytest -v --html=reports/reporte.html
