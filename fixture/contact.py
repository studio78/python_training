from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_all_fields(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.app.return_to_main_page()

    def fill_all_fields(self, contact):
        wd = self.app.wd
        self.app.fill_field_by_name("firstname", contact.firstname)
        self.app.fill_field_by_name("middlename", contact.middlename)
        self.app.fill_field_by_name("lastname", contact.lastname)
        self.app.fill_field_by_name("nickname", contact.nickname)
        self.app.fill_field_by_name("title", contact.title)
        self.app.fill_field_by_name("company", contact.company)
        self.app.fill_field_by_name("address", contact.address)
        self.app.fill_field_by_name("home", contact.home)
        self.app.fill_field_by_name("mobile", contact.mobile)
        self.app.fill_field_by_name("work", contact.work)
        self.app.fill_field_by_name("fax", contact.fax)
        self.app.fill_field_by_name("email", contact.email)
        self.app.fill_field_by_name("email2", contact.email2)
        self.app.fill_field_by_name("email3", contact.email3)
        self.app.fill_field_by_name("homepage", contact.homepage)
        self.app.fill_field_by_name("byear", contact.byear)
        self.app.fill_field_by_name("ayear", contact.ayear)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)

    def delete_first(self):
        wd = self.app.wd
        self.open_home_page()
        # select fist contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.app.open_home_page()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def edit_first(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # edit button fist contact
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        # fill contact form
        self.fill_all_fields(contact)
        # click button Update
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
