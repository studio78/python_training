# -*- coding: utf-8 -*-
from model.contact import Contact
import datahelpers.stringhelper as dh


def test_edit_contact(app):
    d = dh.get_random_string(5)
    if app.contact.count() == 0:
        app.contact.create(dh.get_random_contact())
    app.contact.edit_first(Contact(firstname=d + "-fname", middlename="mname", lastname="lname", nickname="nickname",
                                   title="title", company="company", address="address", home="home",
                                   mobile="mobile", fax="fax", work="work", email="email", email2="email2",
                                   email3="email3", homepage="homepage", bday="1", bmonth="January",
                                   byear="1980", aday="5", amonth="December", ayear="1990"))
