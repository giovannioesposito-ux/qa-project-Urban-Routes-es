# Proyecto qa-project-Urban-Routes-es
Sprint 9
QA Engineer: Giovanni Esposito
Grupo 76a
---

## Descripción del proyecto
Proyecto de automatización de pruebas web end-to-end desarrollado en Python con Selenium WebDriver. Implementa el patrón de diseño Page Object Model (POM) para automatizar el flujo completo de reserva de un transporte en la plataforma Urban Routes.

El código define la clase de página 'UrbanRoutesPage', encargada de mapear los elementos de la interfaz de usuario (localizadores) y encapsular las interacciones necesarias para llevar a cabo el flujo de reserva.

## Formato del proyecto
**data**: contiene todos los datos y rutas necesarios para las prueba. Las rutas deben ser actualizadas antes de realizar las pruebas

**main**: contiene las clases, localizadores, métodos, pasos y funciones de las pruebas.

##  Tecnologías y Técnicas Usadas

### Stack Tecnológico
* **Lenguaje de Programación:** [Python](https://python.org) - Lenguaje principal para la escritura de los scripts de prueba automatizados.
* **Entorno de Desarrollo (IDE):** [PyCharm](https://jetbrains.com) - Editor utilizado para la codificación, depuración y ejecución de las pruebas.
* **Selenium WebDriver:** [Selenium](https://www.selenium.dev) Biblioteca para la automatización de navegadores web y simulación de acciones de usuario.
* **Control de Versiones:** [Git](https://git-scm.com) - Gestión del historial de cambios del código de automatización.
* **Alojamiento del Repositorio:** [GitHub](https://github.com) - Plataforma para almacenar el código del proyecto y permitir la revisión por pares.

### Técnicas de QA y Automatización
* **Patrón de Diseño Page Object Model (POM):** abstracción de la interfaz de usuario en la clase UrbanRoutesPage para separar la localización de elementos web (selectores) de la lógica de negocio e interacción en las pruebas.
* **Localización Dinámica y Robusta de Elementos:** Uso de múltiples estrategias de selección de elementos (By.XPATH, By.CSS_SELECTOR, By.ID, By.CLASS_NAME y By.NAME) priorizando la flexibilidad ante cambios en la interfaz.
* **Manejo de Esperas Explícitas (Explicit Waits):** implementación de WebDriverWait en conjunto con expected_conditions (visibility_of_element_located, element_to_be_clickable, presence_of_element_located) para asegurar la sincronización y la estabilidad en la ejecución frente a la carga de elementos asíncronos.
* **Automatización del Flujo End-to-End (E2E):** Cobertura completa de interacción con formularios web (ingreso de texto, clics, interacción con sliders, switches, contadores de elementos e inserción de tarjetas de crédito).

## Lista de Pruebas automatizadas
[1.] Configurar la dirección.   
[2.] Seleccionar una tarifa (Comfort).  
[3.] Rellenar y validar el campo número de teléfono.   
[4.] Agregar una tarjeta de crédito.   
[5.] Escribir un mensaje para el conductor.  
[6.] Pedir manta y pañuelos.   
[7.] Pedir 2 helados.  
[8.] Solicitar el taxi y que aparezca la modal.  
[9.] Esperar a que aparezca la información del viaje.

## Instrucciones de ejecución de las pruebas
Para ejecutar la suite de pruebas automatizadas del proyecto Urban Routes, sigue estos pasos:

### Requisitos previos:

* Clonar el repositorio:   
 ```bash  
git clone git@github.com:giovannioesposito-ux/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
```

* Tener instalado Python 3.x.
* Disponer de las dependencias instaladas en tu entorno virtual o local:
 ```bash  
pip install selenium
```

* Configurar la URL del servidor:    
    * Inicia el servidor de prueba para obtener la URL activa.    
    * Abre el archivo `data.py`.   
    * Asigna la URL generada (incluyendo `?lng=es`) a la variable `urban_routes_url`.
* Ejecutar el proyecto:    
    * Abre una terminal en la carpeta raíz del proyecto.   
    * Ejecuta el siguiente comando para correr todas las pruebas:   
      ```bash  
      pytest main.py
      ```
    * *(Opcional)* Si prefieres ver el detalle paso a paso en consola, utiliza el modo explícito:   
      ```bash
      pytest -v main.py
      ```

## Dependencias del Proyecto
Package           Version

attrs             26.1.0.  
certifi           2026.7.22.  
h11               0.16.0.  
idna              3.19
iniconfig         2.3.0.  
outcome           1.3.0.post0.  
packaging         26.3.  
pip               26.0.1.  
pluggy            1.6.0.  
Pygments          2.21.0.  
PySocks           1.7.1.  
pytest            9.1.1.  
selenium          4.47.0.  
sniffio           1.3.1.  
sortedcontainers  2.4.0.  
trio              0.34.0.  
trio-websocket    0.12.2.  
typing_extensions 4.16.0.  
urllib3           2.7.0.  
websocket-client  1.9.0.  
wsproto           1.3.2


## Entorno
JetBrains PyCharm 2026.2.0.1 (Build 262.8665.369)
Google Chrome Versión 151.0.7922.109 (Build oficial) (arm64)
