import configparser


def read_config_data(section, key):
    config = configparser.ConfigParser()
    config.read("./Configuration/Config.cfg")
    return config.get(section, key)


def read_elements(section, key):
    config = configparser.ConfigParser()
    config.read("./Configuration/Elements.cfg")
    return config.get(section, key)
