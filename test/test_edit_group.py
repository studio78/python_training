# -*- coding: utf-8 -*-
from model.group import Group
from datahelpers.stringhelper import get_random_string


def test_edit_group(app):
    d = get_random_string(5)
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name=d + "-gname", footer=d + "-gfooter", header=d + "-gheader"))
    app.session.logout()
