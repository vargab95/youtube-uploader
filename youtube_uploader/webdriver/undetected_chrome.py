#!/usr/bin/python3

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    ElementClickInterceptedException
)

from ..webdriver import IWebDriver
from ..webdriver.errors import ElementNotFoundException, ClickFailedException


class UndetectedChromeWebDriver(IWebDriver):
    def __init__(self):
        self.__driver = uc.Chrome()

    def open_page(self, url: str) -> None:
        self.__driver.get(url)

    def set_input_value(self, css_selector: str, value: str, clean_up: bool = True) -> None:
        try:
            if clean_up:
                self.__find_element(css_selector).clear()
            self.__find_element(css_selector).send_keys(value)
        except ElementNotInteractableException:
            element = self.__find_element(css_selector)
            self.__driver.execute_script('arguments[0].style.visibility = "visible";', element)
            self.__driver.execute_script('arguments[0].style.display = "block";', element)
            self.__driver.execute_script('arguments[0].style.height = "500px";', element)
            self.__driver.execute_script('arguments[0].style.width = "500px";', element)
            self.__driver.execute_script('arguments[0].style.opacity = "1";', element)
            self.__driver.execute_script('arguments[0].style.overflow = "visible";', element)
            self.__driver.execute_script('arguments[0].setAttribute("aria-hidden", "false");', element)
            self.__driver.execute_script('arguments[0].removeAttribute("hidden");', element)
            if clean_up:
                self.__find_element(css_selector).clear()
            self.__find_element(css_selector).send_keys(value)

    def click(self, css_selector: str, timeout: int = None) -> None:
        try:
            if timeout is not None:
                wait = WebDriverWait(self.__driver, timeout)
                element = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
                element.click()
            else:
                self.__find_element(css_selector).click()
        except ElementClickInterceptedException as exc:
            raise ClickFailedException from exc

    def select_option_by_text(self, text: str) -> None:
        self.__driver.find_element(By.XPATH, f"//*[text()='{text}']").click()

    def __find_element(self, css_selector: str):
        try:
            return self.__driver.find_element(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException as exc:
            raise ElementNotFoundException from exc

    def wait_for_element(self, css_selector: str, timeout: int = 60) -> None:
        WebDriverWait(self.__driver, timeout=timeout).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
