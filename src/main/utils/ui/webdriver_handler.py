from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep


class WebDriverHandler:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def patiently_switch_to_window(self, position: int = 0):
        i = 0
        while i < 5:
            try:
                self.driver.switch_to.window(self.driver.window_handles[position])
                break
            except IndexError:
                i += 1
            sleep(1)
