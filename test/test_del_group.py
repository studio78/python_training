from model.group import Group
import random
import allure

'''
def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

    
def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
'''


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    with allure.step('Given a random group from the list'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with allure.step('When I delete the group from the list'):
        app.group.delete_group_by_id(group.id)
    with allure.step('Then The new group list is equal to the old list without deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == app.group.count()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
