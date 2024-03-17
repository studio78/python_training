import datahelpers.stringhelper as dh


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(dh.get_random_contact())
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
