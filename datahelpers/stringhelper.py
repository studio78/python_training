import random
import string
from model.group import Group
from model.contact import Contact


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_random_group():
    return Group(name=get_random_string(5), header=get_random_string(5), footer=get_random_string(5))


def get_random_contact():
    return Contact(firstname=get_random_string(5), bday="1", bmonth="January", aday="1", amonth="December")
