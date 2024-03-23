import random
import string
from model.group import Group
from model.contact import Contact


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_random_digits(length):
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(length))


def get_random_phone():
    return "+{}({}){}{}{}-{}{}-{}{}".format(random.randint(1, 9), get_random_digits(3),
                                            *[random.randrange(10) for i in range(7)])


def get_random_email():
    return "{}@{}.{}".format(get_random_string(5), get_random_string(5), get_random_string(2))


def get_random_group():
    return Group(name=get_random_string(5), header=get_random_string(5), footer=get_random_string(5))


def get_random_contact():
    return Contact(lastname=get_random_string(5), firstname=get_random_string(5), address=get_random_string(10),
                   home=get_random_phone(), mobile=get_random_phone(), work=get_random_phone(), fax=get_random_phone(),
                   email=get_random_email(), email2=get_random_email(), email3=get_random_email(),
                   bday="1", bmonth="January", aday="1", amonth="December")
