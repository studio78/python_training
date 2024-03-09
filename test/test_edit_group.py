# -*- coding: utf-8 -*-
from model.group import Group
from datahelpers.stringhelper import get_random_string


def test_edit_group(app):
    d = get_random_string(5)
    app.group.edit_first(Group(name=d + "-gname", footer=d + "-gfooter", header=d + "-gheader"))


def test_edit_group_name(app):
    d = get_random_string(5)
    app.group.edit_first(Group(name=d + "-gname"))


def test_edit_group_header(app):
    d = get_random_string(5)
    app.group.edit_first(Group(header=d + "-gheader"))
