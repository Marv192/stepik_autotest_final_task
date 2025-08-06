from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.XPATH, '//form[@id="register_form"]/div/div/input[@type="email"]')
    REGISTER_PASSWORD = (By.XPATH, '//form[@id="register_form"]/div/div/input[@name="registration-password1"]')
    REGISTER_CONFIRM_PASSWORD = (By.XPATH, '//form[@id="register_form"]/div/div/input[@name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ADDED_PRODUCT_NAME =(By.CSS_SELECTOR, ".alert > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")
