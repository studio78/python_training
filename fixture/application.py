from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        # совсем без ожидания нельзя, тесты не проходят
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/")

    def return_to_main_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def fill_field_by_name(self, name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(text)

    def destroy(self):
        self.wd.quit()
