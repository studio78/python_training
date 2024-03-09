from model.contact import Contact
import datahelpers.stringhelper as dh


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(dh.get_random_contact())
    app.contact.delete_first()
