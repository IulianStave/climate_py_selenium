from src.common.Pages import DataStorePage, HomePage

from src.common.common import BrowserTestCase
from src.data.TestData import TestData
from src.data.Locators import Locators
# from time import sleep


class DataStoreTest(BrowserTestCase):
    def test__cookies_consent(self):
        """ Clicks on cookies consent button
        """
        self.data_store_page = DataStorePage(self.driver)
        cookies_button = self.data_store_page.click(
            Locators.DATA_COOKIES_CONSENT)
        self.assertTrue(cookies_button, 'Cookies consent button click failed')

    def test_access_the_catalogue(self):
        """ Search in the Data Store
        """
        self.data_store_page = HomePage(self.driver)
        self.data_store_page.click(Locators.DATA_LINK)
        data_search_input = self.data_store_page.is_enabled(
            Locators.DATA_SEARCH_INPUT)
        data_search_input.send_keys(TestData.DS_SEARCH_TEXT)
        data_search_submit = self.data_store_page.is_enabled(
            Locators.DATA_SEARCH_SUBMIT)
        data_search_submit.click()
        # sleep(3)
        # print(self.data_store_page.driver.title)
        # print(self.data_store_page.driver.current_url)
        self.data_store_page.wait_title(TestData.SEARCH_DS_TITLE)
        self.assertIn(TestData.SEARCH_DS_TITLE, self.data_store_page.driver.title)
