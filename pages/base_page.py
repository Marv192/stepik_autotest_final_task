from stepik_autotest_final_task.conftest import browser


class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)