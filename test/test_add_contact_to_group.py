import random
import datahelpers.stringhelper as dh


def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(dh.get_random_group())
    contact = dh.get_random_contact()
    app.contact.create(contact)
    contact_from_db = orm.get_contact_by_lastname(contact.lastname)
    group = random.choice(orm.get_group_list())
    contacts_in_group = orm.get_contacts_in_group(group)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    app.contact.add_to_group(contact_from_db.id, group.id)
    assert len(contacts_in_group) + 1 == len(orm.get_contacts_in_group(group))
    assert len(contacts_not_in_group) - 1 == len(orm.get_contacts_not_in_group(group))
