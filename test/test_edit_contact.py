# -*- coding: utf-8 -*-
from model.contact import Contact
from datahelpers.stringhelper import get_random_string


def test_edit_contact(app):
    d = get_random_string(5)
    app.contact.edit_first(Contact(firstname=d + "-fname", middlename="mname", lastname="lname", nickname="nickname",
                                   title="title", company="company", address="address", home="home",
                                   mobile="mobile", fax="fax", work="work", email="email", email2="email2",
                                   email3="email3", homepage="homepage", bday="1", bmonth="January",
                                   byear="1980", aday="5", amonth="December", ayear="1990"))
