from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait
from enum import Enum


class BaseWebElement(object):
    """Base Class that is initialized on every 'Web Element' object"""

    def __init__(self, driver: WebDriver, locator):
        self.driver = driver
        self.full_locator = locator
        self.by = locator[0]
        self.locator = locator[1]

        self.action = ActionChains(driver)
        self.element: WebElement = self.safety_get_element_by(Expectation.PRESENCE)

    def __set__(self, value):
        """Sets the text to the value supplied"""
        self.element.clear()
        self.element.send_keys(value)

    def __get__(self, owner):
        """Gets the text of the specified object"""
        return self.element.get_attribute("value")

    def manually_clear(self):
        self.click()
        self.element.send_keys(Keys.COMMAND + Keys.SHIFT + Keys.ARROW_LEFT)
        self.element.send_keys(Keys.DELETE)

    def click(self):
        """"Safety clicks on an element"""
        element = self.safety_get_element_by(Expectation.CLICKABLE)
        element.click()

    def hover(self):
        """Safety hovers on an element"""
        element = self.safety_get_element_by(Expectation.VISIBILITY)
        self.action.move_to_element(element).perform()

    def simulate_click(self):
        self.action.click(self.element)

    def get_text(self) -> str:
        self.safety_get_element_by(Expectation.VISIBILITY)
        return self.element.text

    def get_amount(self) -> float:
        content = self.get_text()
        if content.__contains__("$"):
            return float(content.replace("$", ""))

    def get_attribute_value(self, att_name) -> str:
        value = self.element.get_attribute(att_name)
        if value is not None:
            return value
        else:
            raise Exception("Unable to find expected attribute value for element with locator " + self.full_locator)

    def get_input_value(self):
        return self.get_attribute_value("value")

    def is_checkbox_on(self) -> bool:
        return self.get_attribute_value("checked") is not None

    def is_displayed(self):
        self.safety_get_element_by(Expectation.VISIBILITY)
        return True

    def is_hidden(self):
        self.safety_get_element_by(Expectation.INVISIBILITY)
        return True

    def safety_get_element_by(self, expected_condition):
        """Safety returns an element after waiting for an element's expected condition (presence, visibility, etc)"""
        driver = self.driver

        try:
            if expected_condition is Expectation.PRESENCE:
                WebDriverWait(driver, 20).until(expected.presence_of_element_located(self.full_locator))
            elif expected_condition is Expectation.VISIBILITY:
                WebDriverWait(driver, 20).until(expected.visibility_of_element_located(self.full_locator))
            elif expected_condition is Expectation.INVISIBILITY:
                WebDriverWait(driver, 20).until(expected.invisibility_of_element(self.full_locator))
            elif expected_condition is Expectation.CLICKABLE:
                WebDriverWait(driver, 20).until(expected.element_to_be_clickable(self.full_locator))
            elif expected_condition is Expectation.ELEMENT_SELECTED:
                WebDriverWait(driver, 20).until(expected.element_to_be_selected(self.full_locator))
            else:
                raise Exception("Illegal State Error>> Invalid Expectation used")

            return driver.find_element(self.by, self.locator)
        except TimeoutException:
            raise TimeoutException("Expected condition for element not complied. Waited for 20 seconds for element with"
                                   " locator pair [" + self.by + ", " + self.locator + "] to be "
                                   + expected_condition.value)


class VisualWebElement(BaseWebElement):
    """Base Class that is initialized on every Visual 'Web Element' object"""

    def __init__(self, driver: WebDriver, locator):
        super().__init__(driver, locator)
        self.element = self.safety_get_element_by(Expectation.VISIBILITY)


class GenericWebElement(VisualWebElement):

    def __init__(self, driver: WebDriver, locator: tuple, template: str, enum: Enum = None, subs_value: str = ""):
        """Creates a Web Element from a Generic Locator by provided both template and enum
        :param driver: WebDriver instance
        :param locator: Generic Locator for re-usability purpose
        :param template: Template pattern to be replaced in locator string
        :param enum: Enumerator with Value to use for specify item to be located
        :param subs_value: String value to be used instead of enum"""
        if enum is not None:
            super().__init__(driver, (locator[0], locator[1].replace(template, str(enum.value))))
        elif subs_value is not "":
            super().__init__(driver, (locator[0], locator[1].replace(template, subs_value)))
        else:
            raise Exception("Invalid Parameter Set for Initializer: 'enum' or 'subs_value' are mutually exclusive "
                            "but setting one of them is required. Please review GenericWebElement __init__()")


class DropdownWebElement(BaseWebElement):
    """Base Class that is initialized on every Dropdown 'Web Element' object for handling purposes"""

    def __init__(self, driver: WebDriver, locator):
        super().__init__(driver, locator)
        self.element = self.safety_get_element_by(Expectation.CLICKABLE)

    def select_option(self, option_locator: tuple, template: str, option: Enum):
        self.click()

        option = GenericWebElement(self.driver, option_locator, template, option)
        option.click()


class Expectation(Enum):
    """Set of supported expectation strategies"""

    PRESENCE = "present"
    VISIBILITY = "visible"
    INVISIBILITY = "invisible"
    CLICKABLE = "click-able"
    ELEMENT_SELECTED = "selected"
