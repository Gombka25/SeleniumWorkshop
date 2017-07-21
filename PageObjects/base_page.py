from selenium.webdriver.ie import webdriver


class BasePage:
    def __init__(self, driver: webdriver.WebDriver):
        self.driver = driver
