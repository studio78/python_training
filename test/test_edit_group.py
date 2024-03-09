# -*- coding: utf-8 -*-
from model.group import Group
import datahelpers.stringhelper as dh


def test_edit_group(app):
    d = dh.get_random_string(5)
    if app.group.count() == 0:
        app.group.create(dh.get_random_group())
    app.group.edit_first(Group(name=d + "-gname", footer=d + "-gfooter", header=d + "-gheader"))


def test_edit_group_name(app):
    d = dh.get_random_string(5)
    if app.group.count() == 0:
        app.group.create(dh.get_random_group())
    app.group.edit_first(Group(name=d + "-gname"))


def test_edit_group_header(app):
    d = dh.get_random_string(5)
    if app.group.count() == 0:
        app.group.create(dh.get_random_group())
    app.group.edit_first(Group(header=d + "-gheader"))
