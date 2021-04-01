from Base import InitiateDriver
from Library import ConfigReader


def test_search_invalid_data():
    driver = InitiateDriver.start_browser()
    driver.find_element_by_xpath(ConfigReader.read_elements('Search', 'search_icon')).click()
    driver.find_element_by_xpath(ConfigReader.read_elements('Search', 'search_textbox')).send_keys('invalid')
    driver.find_element_by_xpath(ConfigReader.read_elements('Search', 'search_button')).click()
    driver.close()
