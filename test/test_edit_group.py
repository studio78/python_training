# -*- coding: utf-8 -*-
from model.group import Group
import datahelpers.stringhelper as dh
# from random import randrange
import random


def test_edit_group(app, db):
    d = dh.get_random_string(5)
    if len(db.get_group_list()) == 0:
        app.group.create(dh.get_random_group())
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    old_groups.remove(old_group)
    group = Group(id=old_group.id, name=d + "-gname", footer=d + "-gfooter", header=d + "-gheader")
    app.group.edit_by_id(group.id, group)
    old_groups.append(group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


'''
def test_edit_group(app):
    d = dh.get_random_string(5)
    if app.group.count() == 0:
        app.group.create(dh.get_random_group())
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name=d + "-gname", footer=d + "-gfooter", header=d + "-gheader")
    group.id = old_groups[index].id
    app.group.edit_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
'''

'''
def test_edit_group_name(app):
    d = dh.get_random_string(5)
    if app.group.count() == 0:
        app.group.create(dh.get_random_group())
    old_groups = app.group.get_group_list()
    group = Group(name=d + "-gname")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_edit_group_header(app):
    d = dh.get_random_string(5)
    if app.group.count() == 0:
        app.group.create(dh.get_random_group())
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(header=d + "-gheader"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
'''