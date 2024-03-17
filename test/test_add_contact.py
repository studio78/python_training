# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fname", middlename="mname", lastname="lname", nickname="nickname",
                      title="title", company="company", address="address", home="home",
                      mobile="mobile", fax="fax", work="work", email="email", email2="email2",
                      email3="email3", homepage="homepage", bday="1", bmonth="January",
                      byear="1980", aday="5", amonth="December", ayear="1990")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


'''
def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                      mobile="", fax="", work="", email="", email2="", email3="", homepage="", bday="-", bmonth="-",
                      byear="", aday="-", amonth="-", ayear="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
'''