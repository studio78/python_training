# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import datahelpers.stringhelper as dh


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                    mobile="", fax="", work="", email="", email2="", email3="", homepage="", bday="-", bmonth="-",
                    byear="", aday="-", amonth="-", ayear="")] + [dh.get_random_contact() for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
