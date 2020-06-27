from random import randrange

from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from datetime import date, timedelta
import logging
import allure


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.display_cookies_xpath = "//a[contains(text(),'Odrzuć')]"
        self.language_select_xpath = "//a[@class='popover_trigger']"
        self.en_language_xpath = "//li[@class='lang_en-gb']"
        self.search_hotel_input_id = "ss"
        self.location_match_span_xpath = "//span[@class='search_hl_name']"
        self.data_range_switch_on_div_xpath = "//div[@class='bui-calendar__control bui-calendar__control--next']"
        date_today = date.today() + timedelta(7)
        self.date_check_in = date_today.strftime("%#d %B %Y")
        self.date_check_out = (date_today + timedelta(10)).strftime("%#d %B %Y")
        self.data_check_in_input_xpath = "//td[@class='bui-calendar__date']//span[contains(@aria-label,'" + str(
            self.date_check_in) + "')]"
        self.data_check_out_input_xpath = "//td[@class='bui-calendar__date']//span[contains(@aria-label,'" + str(
            self.date_check_out) + "')]"
        self.travellers_input_id = "xp__guests__toggle"
        self.travellers_frame_check_xpath = "//label[@id='xp__guests__toggle'][@aria-expanded='true']"
        self.adult_input_xpath = "//div[@class='sb-group__field sb-group__field-adults']" \
                                 "//button[contains(@class,'subtract-button')]"
        self.children_input_xpath = "//div[contains(@class,'sb-group__field sb-group-children')]" \
                                    "//button[contains(@class,'add-button')]"
        self.children_age_input_name = "age"
        self.search_button_name = "xp__button"

    @allure.step("Odrzucenie zgody na wyświetlanie plików cookies")
    def set_cookies(self):
        self.logger.info("Odrzucam wyświetlanie plików cookies ")
        while True:
            try:
                self.driver.find_element_by_xpath(self.display_cookies_xpath).click()
                self.logger.info("Wyświetlanie plików cookies jest widoczne ")

            except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
                self.logger.info("Wyświetlanie plików cookies NIE jest widoczne ")
            break

    @allure.step("Zmiana języka strony z polskiego na angielski")
    def set_change_language(self):
        self.logger.info("Zmieniam język strony na angielski")
        self.driver.find_element_by_xpath(self.language_select_xpath).click()
        self.driver.find_element_by_xpath(self.en_language_xpath).click()

    @allure.step("Wprowadzenie nazwy miasta {1}")
    def set_city(self, city):
        self.logger.info("Ustawiam miasto {}".format(city))
        self.driver.find_element_by_id(self.search_hotel_input_id).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_span_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_city", attachment_type=AttachmentType.PNG)

    @allure.step("Ustawienie daty zameldowania  i wymeldowania ")
    def set_date_range(self):
        self.logger.info("Ustawiam datę zameldowania {checkin} i wymeldowania {checkout} "
                         .format(checkin=self.date_check_in, checkout=self.date_check_out))
        self.driver.find_element_by_xpath(self.data_check_in_input_xpath).click()
        self.driver.find_element_by_xpath(self.data_check_out_input_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_date_range", attachment_type=AttachmentType.PNG)
        return self.date_check_in, self.date_check_out

    @allure.step("Uruchomienie ramki wyboru osób. Wybór ilości dorosłych, dzieci i wieku dzieci ")
    def set_travellers_range(self):

        try:
            self.driver.find_element_by_xpath(self.travellers_frame_check_xpath)
            print("Is eneble")

        except NoSuchElementException:

            print("Is disable so I click on it")
            self.driver.find_element_by_id(self.travellers_input_id).click()

        self.driver.find_element_by_xpath(self.adult_input_xpath).click()
        add_child_button = self.driver.find_element_by_xpath(self.children_input_xpath)
        add_child_button.click()
        add_child_button.click()
        children = self.driver.find_elements_by_name(self.children_age_input_name)
        count_child = str(len(children))
        for child in children:
            child.location_once_scrolled_into_view
            child.click()
            child.send_keys(randrange(18))
            child.click()
        self.logger.info("Sprawdzam czy ramka ustawień jest uruchomiona,"
                         "ustawiam osobę dorosłą i {children} dzieci  ".format(children=count_child))
        allure.attach(self.driver.get_screenshot_as_png(), name="set_travellers_range",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Uruchomienie Wyszukiwania noclegów")
    def perform_search(self):
        self.logger.info("Uruchamiam wyszukiwanie")
        self.driver.find_element_by_class_name(self.search_button_name).click()
