from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_all_fields(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.app.return_to_main_page()
        self.contact_cache = None

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
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # select contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # submit deletion
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.app.open_home_page()
        self.contact_cache = None

    def add_to_group(self, id, group_id):
        wd = self.app.wd
        self.open_home_page()
        # select contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # select group
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)
        # click button Add to
        wd.find_element_by_name("add").click()
        self.open_home_page()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def edit_first(self, contact):
        self.edit_by_index(0, contact)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # edit button contact by index
        wd.find_elements_by_xpath('//*[@title="Edit"]')[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # edit button contact by index
        wd.find_element_by_xpath('//input[@id="%s"]//..//..//*[@title="Edit"]' % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath('//*[@title="Details"]')[index].click()

    def edit_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # fill contact form
        self.fill_all_fields(contact)
        # click button Update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        # fill contact form
        self.fill_all_fields(contact)
        # click button Update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                column = element.find_elements_by_tag_name("td")
                all_emails = column[4].text
                ''' 
                в списке контактов отсутствует телефон fax, по этому в поле all_phones_from_home_page будeт 
                телефоны: home, mobile, work
                '''
                all_phones = column[5].text
                self.contact_cache.append(Contact(lastname=column[1].text, firstname=column[2].text, id=id,
                                                  address=column[3].text, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, home=home, mobile=mobile, work=work, fax=fax, id=id,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, fax=fax)

    def filter_contacts_by_group_id(self, group_id):
        wd = self.app.wd
        self.open_home_page()
        # select group
        Select(wd.find_element_by_name("group")).select_by_value(group_id)

    def remove_from_group_by_id(self, id):
        wd = self.app.wd
        # select contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # remove
        wd.find_element_by_name('remove').click()
        self.app.open_home_page()
        self.contact_cache = None