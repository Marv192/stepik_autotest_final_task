from stepik_autotest_final_task.pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "basket is not empty"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "no empty basket text"
