# -*- coding: utf-8 -*-
from model.group import Group
# import datahelpers.stringhelper as dh

testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2"),
]

# testdata = [Group(name="", footer="", header="")] + [dh.get_random_group() for i in range(5)]
