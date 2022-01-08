#!/usr/bin/python3

import abc


class IWebDriver:
    @abc.abstractmethod
    def open_page(self, url: str) -> None:
        pass

    @abc.abstractmethod
    def set_input_value(self, css_selector: str, value: str, clean_up: bool = True) -> None:
        pass

    @abc.abstractmethod
    def click(self, css_selector: str, timeout: int = None) -> None:
        pass

    @abc.abstractmethod
    def select_option_by_text(self, text: str) -> None:
        pass

    @abc.abstractmethod
    def wait_for_element(self, css_selector: str, timeout: int = 60) -> None:
        pass
