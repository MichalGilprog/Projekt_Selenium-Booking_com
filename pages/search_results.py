import logging
import re
import allure
from allure_commons.types import AttachmentType


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.hotel_result_set_xpath = "//div[@id='hotellist_inner']/div[contains(@class,'sr_flex_layout')]"
        self.hotel_prices_xpath = "//div[contains(@class,'prc-d-sr-wrapper')]" \
                                  "//div[contains(@class,'bui-price-display__value')]"
        self.hotel_price_currency_plinktext = "zł"
        self.hotel_city_correct_results_xpath = "//div[@id='hotellist_inner']//a[contains(text(),'Hel')]"
        self.correct_city_result_xpath = "//h1[contains(text(),'Hel')]"

    @allure.step("Pobieramy ilość pensjonatów wyświetlanych na stronie")
    def get_number_of_hotels(self):
        number_hotels = self.driver.find_elements_by_xpath(self.hotel_result_set_xpath)
        self.logger.info("Sprawdzam wyświwetlaną na stronie liczbę pensjonatów: " + str(len(number_hotels)))
        allure.attach(self.driver.get_screenshot_as_png(), name="get_number_of_hotels",
                      attachment_type=AttachmentType.PNG)
        return len(number_hotels)

    @allure.step("Wyświetlamy w jakiej walucie powinna być cena rezerwacji")
    def check_hotel_polish_prices(self):
        prices = self.driver.find_elements_by_xpath(self.hotel_prices_xpath)
        price_values = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Sprawdzam czy kwota za rezerwacji jest podana we właściwej walucie: ")

        for hotel_price in price_values:
            self.logger.info(hotel_price[-3:-1])
            return hotel_price[-3:-1]

    def currency_set(self):
        self.logger.info("Sprawdzam czy kwota za wynajem jest podana we właściwej walucie 'zł'")
        return self.driver.find_element_by_partial_link_text(self.hotel_price_currency_plinktext)

    @allure.step("Wyświetlamy jaka jest liczba pensjonatów miejscowości która nas interesuje")
    def get_city_results(self):
        Hel_results = self.driver.find_elements_by_xpath(self.hotel_city_correct_results_xpath)
        self.logger.info("Liczba pensjonatów z właściwą lokalizacją na Helu: " + str(len(Hel_results)))
        return len(Hel_results)

    @allure.step("Sprawdzamy czy liczba pensjonatów z szukanej miejscowości jest zgodna z opisem ")
    def get_count_correct_city(self):
        count_correct_city = self.driver.find_element_by_xpath(self.correct_city_result_xpath)
        get_city_number = int((re.search(r'\d+', count_correct_city.text).group(0)))
        self.logger.info("Komunikat o wynikach dla szukanego miasta: " + count_correct_city.get_attribute("textContent"))
        return get_city_number
