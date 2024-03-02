# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="fname", middlename="mname", lastname="lname", nickname="nickname",
                               title="title", company="company", address="address", home="home",
                               mobile="mobile", fax="fax", work="work", email="email", email2="email2",
                               email3="email3", homepage="homepage", bday="1", bmonth="January",
                               byear="1980", aday="5", amonth="December", ayear="1990"))


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home="",
                               mobile="", fax="", work="", email="", email2="",
                               email3="", homepage="", bday="-", bmonth="-",
                               byear="", aday="-", amonth="-", ayear=""))
