# -*- coding: utf-8 -*-
from model.contact import Contact
import datahelpers.stringhelper as dh
import random


def test_edit_contact(app, db):
    d = dh.get_random_string(5)
    if len(db.get_contact_list()) == 0:
        app.contact.create(dh.get_random_contact())
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    old_contacts.remove(old_contact)
    contact = Contact(id=old_contact.id, firstname=d + "-fname", middlename="mname", lastname="lname",
                      nickname="nickname", title="title", company="company", address="address", home="home",
                      mobile="mobile", fax="fax", work="work", email="email", email2="email2", email3="email3",
                      homepage="homepage", bday="1", bmonth="January", byear="1980", aday="5", amonth="December",
                      ayear="1990")
    app.contact.edit_by_id(old_contact.id, contact)
    old_contacts.append(contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
