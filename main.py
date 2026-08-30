import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    #Localizadores Prueba 1
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    #Localizalizadores Prueba 2
    mode_personal = (By.XPATH, f"//div[contains(@class, 'modes-container')]//div[text()='Personal']")
    icon_taxi = (By.CSS_SELECTOR, "img.type-icon[src*='taxi']")
    boton_pedir_taxi = (By.XPATH, "//button[contains(@class, 'button') and text()='Pedir un taxi']")
    comfort_tarriff = (By.XPATH, f"//div[contains(@class, 'tcard') and .//div[@class='tcard-title' and text()='Comfort']]")

    #Localizadores Prueba 3
    cellphone_field = (By.CSS_SELECTOR, '.np-text')
    popup_phone_field = (By.NAME, 'phone')
    popup_boton_siguiente = (By.XPATH, "//button[@type='submit' and text()='Siguiente']")
    phone_code_field = (By.ID, 'code')
    code_confirm_button = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")

    #Localizadores Prueba 4
    payment_method = (By.CSS_SELECTOR, '.pp-text')
    add_payment_card = (By.CSS_SELECTOR, '.pp-plus')
    card_number_field = (By.CSS_SELECTOR, "#number.card-input")
    card_code_field = (By.CSS_SELECTOR, "#code.card-input")
    confirm_card_button = (By.CSS_SELECTOR, '.pp-buttons button[type="submit"]')
    form_payment_method = (By.CLASS_NAME, 'section')
    exit_payment_button = (By.CSS_SELECTOR, ".payment-picker .section.active:not(.unusual) .close-button")
    payment_field_text = (By.CLASS_NAME, "pp-value-text")
    payment_form = (By.XPATH, "//div[contains(@class, 'section') and .//div[text()='Método de pago']]")

    #Localizadores Prueba 5
    message_field = (By.NAME, 'comment')

    #Localizadores Prueba 6
    slider_manta = (By.CSS_SELECTOR, ".reqs-body > .r:nth-child(1) .slider")
    status_checkbox_manta = (By.CSS_SELECTOR, ".reqs-body > .r:nth-of-type(1) .switch-input")

    #Localizadores Prueba 7
    add_button_icecream = (By.XPATH, "//div[.='Helado']/following-sibling::div//div[text()='+']")
    quantity_of_icecream = (By.XPATH, "//div[.='Helado']/following-sibling::div//div[contains(@class, 'counter-value')]")

    #Localizadores Prueba 8
    smart_button_text = (By.XPATH, f"//span[@class='smart-button-main' and contains(text(), 'Pedir')]")
    order_taxi_header = (By.CSS_SELECTOR, 'div.order-header-title')

    #Localizadores Prueba 9
    order_taxi_number = (By.CLASS_NAME, 'order-number')

    def __init__(self, driver):
        self.driver = driver

    #Métodos de Prueba 1. Configurar la dirección
    def set_from(self, from_address):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route (self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    #Métodos de Prueba 2. Seleccionar la tarifa Comfort
    def click_mode_personal(self):
        self.driver.find_element(*self.mode_personal).click()

    def get_class_mode_personal(self):
        return self.driver.find_element(*self.mode_personal).get_attribute('class')

    def click_taxi_icon(self):
        self.driver.find_element(*self.icon_taxi).click()

    def get_taxi_icon_father_class(self):
        taxi = self.driver.find_element(*self.icon_taxi)
        return taxi.find_element(By.XPATH, "..").get_attribute("class")

    def click_boton_pedir_un_taxi(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.boton_pedir_taxi))
        self.driver.find_element(*self.boton_pedir_taxi).click()

    def get_class_tarifa_comfort(self):
        return self.driver.find_element(*self.comfort_tarriff).get_attribute('class')

    def click_boton_select_tarifa_comfort(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.comfort_tarriff))
        self.driver.find_element(*self.comfort_tarriff).click()

    # Métodos de Prueba 3. Rellenar el número de teléfono.
    def click_phone_field(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.cellphone_field))
        self.driver.find_element(*self.cellphone_field).click()

    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.popup_phone_field))
        self.driver.find_element(*self.popup_phone_field).send_keys(phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.popup_boton_siguiente).click()

    def get_phone_value(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.cellphone_field))
        return self.driver.find_element(*self.cellphone_field).text

    def new_phone_number(self, new_phone_number):
        self.click_phone_field()
        self.set_phone_number(new_phone_number)

    def click_confirm_code(self):
        self.driver.find_element(*self.code_confirm_button).click()

    def set_phone_code(self):
        phone_code = retrieve_phone_code(driver=self.driver)
        self.driver.find_element(*self.phone_code_field).send_keys(phone_code)
        self.click_confirm_code()

    #Métodos de Prueba 4. Agregar una tarjeta de crédito
    def click_payment_field(self):
        self.driver.find_element(*self.payment_method).click()

    def click_add_new_card_button(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.add_payment_card))
        self.driver.find_element(*self.add_payment_card).click()

    def set_credit_card_number(self, credit_card_number):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.card_number_field))
        self.driver.find_element(*self.card_number_field).click()
        self.driver.find_element(*self.card_number_field).send_keys(credit_card_number)

    def set_credit_card_code(self, credit_card_code):
        self.driver.find_element(*self.card_code_field).click()
        self.driver.find_element(*self.card_code_field).send_keys(credit_card_code)
        self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)

    def click_confirm_card_form (self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.confirm_card_button))
        self.driver.find_element(*self.confirm_card_button).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.confirm_card_button))

    def click_exit_payment_selection(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.exit_payment_button)).click()

    def get_payment_field_text(self):
        return self.driver.find_element(*self.payment_field_text).text

    def add_new_card_info (self, card_number, card_code):
        self.click_payment_field()
        self.click_add_new_card_button()
        self.set_credit_card_number(card_number)
        self.set_credit_card_code(card_code)
        self.click_confirm_card_form()
        self.click_exit_payment_selection()

    #Métodos de Prueba 5. Escribir un mensaje para el conductor
    def click_message_label (self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.message_field)).click

    def set_message_field(self, message_text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.message_field))
        self.driver.find_element(*self.message_field).clear()
        self.driver.find_element(*self.message_field).send_keys(message_text)

    def get_message_field_text(self):
        return self.driver.find_element(*self.message_field).get_attribute('value')

    def add_a_message (self, comment_text):
        self.click_message_label()
        self.set_message_field(comment_text)

    #Métodos de Prueba 6. Solicitar manta y pañuelos
    def click_add_manta_y_panuelos(self):
        self.driver.find_element(*self.slider_manta).click()

    def get_status_manta_y_panuelos(self):
        return self.driver.find_element(*self.status_checkbox_manta).is_selected()

    #Métodos de Prueba 7. Solicitar 2 helados
    def get_quantity_of_icecream(self):
        quantity_of_icecream_txt =  self.driver.find_element(*self.quantity_of_icecream).text
        return int(quantity_of_icecream_txt)

    def click_add_more_icecream (self):
        self.driver.find_element(*self.add_button_icecream).click()

    def request_x_amount_of_icecream(self, amount_of_icecream):
        while (self.get_quantity_of_icecream() < amount_of_icecream):
            self.click_add_more_icecream()

    #Métodos de Prueba 8. Aparece la modal para buscar taxi
    def get_smart_button_txt(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.smart_button_text))
        return self.driver.find_element(*self.smart_button_text).text

    def click_smart_button(self):
        self.driver.find_element(*self.smart_button_text).click()

    def get_modal_header(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.order_taxi_header))
        return self.driver.find_element(*self.order_taxi_header).text

    #Métodos de Prueba 9. Aparece la info del taxi en la modal
    def get_taxi_order_number(self):
        return WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(self.order_taxi_number))

    def waiting_for_driver(self):
        taxi_order = self.get_taxi_order_number().is_displayed()
        return taxi_order


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        """from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)"""

        #Elemento de archivo anterior para los registros estaba obsoleto, se cambio por lo siguiente:
        from selenium.webdriver.chrome.options import Options

        # 1. Crear la instancia de Options
        options = Options()

        # 2. Configurar las preferencias de logging usando set_capability
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # 3. Inicializar el driver pasando las opciones
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort_price(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_mode_personal()
        class_mode_personal = routes_page.get_class_mode_personal()
        assert 'active' in class_mode_personal.split(), f"Se esperaba que el modo personal estuviera activo"

        routes_page.click_taxi_icon()
        class_father_icon = routes_page.get_taxi_icon_father_class()
        assert 'active' in class_father_icon.split(), f"Se esperaba que se seleccionara taxi como modo de transporte"
        routes_page.click_boton_pedir_un_taxi()

        routes_page.click_boton_select_tarifa_comfort()
        class_tarifa_comfort = routes_page.get_class_tarifa_comfort()
        assert 'active' in class_tarifa_comfort.split(), f"Se esperaba que se seleccionara la tarifa comfort"

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.new_phone_number(phone_number)
        routes_page.click_next_button()
        routes_page.set_phone_code()
        assert routes_page.get_phone_value() == phone_number

    def test_fill_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_new_card_info(card_number, card_code)
        assert routes_page.get_payment_field_text() == 'Tarjeta'

    def test_fill_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.add_a_message(message_for_driver)
        assert routes_page.get_message_field_text() == message_for_driver

    def test_add_request(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_manta_y_panuelos()
        assert routes_page.get_status_manta_y_panuelos()

    def test_add_2_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        amount_of_icecream_requested = data.request_icecream
        routes_page.request_x_amount_of_icecream(amount_of_icecream_requested)
        assert amount_of_icecream_requested == routes_page.get_quantity_of_icecream()

    def test_modal_looking_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        smart_button_txt = data.smart_button_txt
        looking_for_taxi_modal_txt = data.looking_for_taxi_modal_txt
        assert smart_button_txt == routes_page.get_smart_button_txt()
        routes_page.click_smart_button()
        assert looking_for_taxi_modal_txt == routes_page.get_modal_header()

    def test_opcional_wait_for_driver_info(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.waiting_for_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
