import data
import pages
from selenium import webdriver

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
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_comfort_price(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
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
        routes_page = pages.UrbanRoutesPage(self.driver)
        phone_number = data.PHONE_NUMBER
        routes_page.new_phone_number(phone_number)
        routes_page.click_next_button()
        routes_page.set_phone_code()
        assert routes_page.get_phone_value() == phone_number

    def test_fill_payment_method(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        card_number = data.CARD_NUMBER
        card_code = data.CARD_CODE
        routes_page.add_new_card_info(card_number, card_code)
        assert routes_page.get_payment_field_text() == 'Tarjeta'

    def test_fill_message(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        message_for_driver = data.MESSAGE_FOR_DRIVER
        routes_page.set_message_field(message_for_driver)
        assert routes_page.get_message_field_text() == message_for_driver

    def test_add_request(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.click_add_manta_y_panuelos()
        assert routes_page.get_status_manta_y_panuelos()

    def test_add_2_icecream(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        amount_of_icecream_requested = data.REQUEST_ICECREAM
        routes_page.request_x_amount_of_icecream(amount_of_icecream_requested)
        assert amount_of_icecream_requested == routes_page.get_quantity_of_icecream()

    def test_modal_looking_for_driver(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        smart_button_txt = data.SMART_BUTTON_TXT
        looking_for_taxi_modal_txt = data.LOOKING_FOR_TAXI_MODAL_TXT
        assert smart_button_txt == routes_page.get_smart_button_txt()
        routes_page.click_smart_button()
        assert looking_for_taxi_modal_txt == routes_page.get_modal_header()

    def test_opcional_wait_for_driver_info(self):
        routes_page = pages.UrbanRoutesPage(self.driver)
        assert routes_page.waiting_for_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
