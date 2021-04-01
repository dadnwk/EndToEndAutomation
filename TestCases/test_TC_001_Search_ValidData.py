from Base import InitiateDriver
from Library import ConfigReader
from Library import ExcelDataGenerator
from Pages import SearchPage
import pytest

# def data_generator():
#     li = ['nike', 'jordon', 'adidas']
#     return li


@pytest.mark.parametrize('data', ExcelDataGenerator.data_generator())
def test_search_valid_data(data):
    driver = InitiateDriver.start_browser()
    search = SearchPage.SearchPage(driver)
    driver.find_element_by_xpath(ConfigReader.read_elements('Search', 'search_icon')).click()
    search.enter_key(data[0])
    driver.find_element_by_xpath(ConfigReader.read_elements('Search', 'search_button')).click()
    driver.close()
