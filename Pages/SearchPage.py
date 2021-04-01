from Library import ConfigReader


class SearchPage:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_key(self, key):
        driver.find_element_by_xpath(ConfigReader.read_elements('Search', 'search_textbox')).send_keys(key)