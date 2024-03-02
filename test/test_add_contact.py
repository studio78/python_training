# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="fname", middlename="mname", lastname="lname", nickname="nickname",
                               title="title", company="company", address="address", home="home",
                               mobile="mobile", fax="fax", work="work", email="email", email2="email2",
                               email3="email3", homepage="homepage", bday="1", bmonth="January",
                               byear="1980", aday="5", amonth="December", ayear="1990"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home="",
                               mobile="", fax="", work="", email="", email2="",
                               email3="", homepage="", bday="-", bmonth="-",
                               byear="", aday="-", amonth="-", ayear=""))
    app.session.logout()
