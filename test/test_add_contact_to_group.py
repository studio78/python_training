import random
import datahelpers.stringhelper as dh


def test_add_contact_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(dh.get_random_group())
    if len(orm.get_contact_list()) == 0:
        app.contact.create(dh.get_random_contact())
    contact = random.choice(orm.get_contact_list())
    group = random.choice(orm.get_group_list())
    app.contact.add_to_group(contact.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)

