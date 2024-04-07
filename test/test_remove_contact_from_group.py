import random
import datahelpers.stringhelper as dh


def test_remove_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        group = dh.get_random_group()
        app.group.create(group)
    if len(orm.get_contact_list()) == 0:
        contact = dh.get_random_contact()
        app.contact.create(contact)
    group = None
    for g in orm.get_group_list():
        if len(orm.get_contacts_in_group(g)) > 0:
            group = g
            break
    if group is None:
        group = orm.get_group_list()[0]
        app.contact.add_to_group(orm.get_contact_list()[0].id, group.id)

    contacts_in_group = orm.get_contacts_in_group(group)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts_in_group)
    app.contact.filter_contacts_by_group_id(group.id)
    app.contact.remove_from_group_by_id(contact.id)
    assert len(contacts_in_group) - 1 == len(orm.get_contacts_in_group(group))
    assert len(contacts_not_in_group) + 1 == len(orm.get_contacts_not_in_group(group))
