# -*- coding: utf-8 -*-
from model.contact import Contact
import datahelpers.stringhelper as dh
from random import randrange


def test_edit_contact(app):
    d = dh.get_random_string(5)
    if app.contact.count() == 0:
        app.contact.create(dh.get_random_contact())
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname=d + "-fname", middlename="mname", lastname="lname", nickname="nickname",
                                   title="title", company="company", address="address", home="home",
                                   mobile="mobile", fax="fax", work="work", email="email", email2="email2",
                                   email3="email3", homepage="homepage", bday="1", bmonth="January",
                                   byear="1980", aday="5", amonth="December", ayear="1990")
    contact.id = old_contacts[index].id
    app.contact.edit_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

