import pytest
from pages.search_hotel import SearchHotelPage
from pages.search_results import SearchResultsPage
import allure

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestHotelSearch(BaseTest):

    @allure.title("Booking.com website test")
    @allure.description("Testowanie strony wyboru pensjonatu w miejscowności Hel ")
    def test_hotel_search(self, setup):
        self.driver.get("https://www.booking.com/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_cookies()
        search_hotel_page.set_change_language()
        search_hotel_page.set_city("Hel")
        search_hotel_page.set_date_range()
        search_hotel_page.set_travellers_range()
        search_hotel_page.perform_search()
        results_page = SearchResultsPage(self.driver)
        quantity_hotels_page = results_page.get_number_of_hotels()
        price_currency = results_page.check_hotel_polish_prices()
        pln_currency = results_page.currency_set()
        correct_city_hotels = results_page.get_city_results()
        num_valid_city = results_page.get_count_correct_city()

        assert quantity_hotels_page == 25
        assert (price_currency_score == pln_currency.text for price_currency_score in price_currency)
        assert correct_city_hotels == num_valid_city
