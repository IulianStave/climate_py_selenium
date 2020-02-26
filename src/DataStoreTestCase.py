from src.common.Pages import DataStorePage, HomePage
from src.common.common import BrowserTestCase
from src.data.TestData import TestData
from src.data.Locators import Locators


class DataStoreTest(BrowserTestCase):
    def test__cookies_consent(self):
        """ Clicks on cookies consent button on Climate Data Store
        """
        self.data_store_page = DataStorePage(self.driver)
        cookies_button = self.data_store_page.click(
            Locators.DATA_COOKIES_CONSENT)
        self.assertTrue(cookies_button, 'Cookies consent button click failed')

    def test_access_the_catalogue(self):
        """ Search in the Climate Data Store
        """
        self.data_store_page = HomePage(self.driver, self.url)
        self.data_store_page.click(Locators.DATA_LINK)
        data_search_input = self.data_store_page.is_enabled(
            Locators.DATA_SEARCH_INPUT)
        data_search_input.send_keys(TestData.DS_SEARCH_TEXT)
        data_search_submit = self.data_store_page.is_enabled(
            Locators.DATA_SEARCH_SUBMIT)
        data_search_submit.click()
        self.data_store_page.wait_title(TestData.SEARCH_DS_TITLE)
        self.assertIn(TestData.SEARCH_DS_TITLE, self.data_store_page.driver.title)
