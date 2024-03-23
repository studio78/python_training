import random
import string
from model.group import Group
from model.contact import Contact
from enums.letter import Letter


def get_random_string(length, letter=None):
    rus_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if letter == Letter.eng or letter is None:
        letters = string.ascii_letters
    elif letter == Letter.dig:
        letters = string.digits
    elif letter == Letter.eng_rus:
        letters = rus_letters + string.ascii_letters
    elif letter == Letter.eng_rus_dig:
        letters = rus_letters + string.ascii_letters + string.digits
    elif letter == Letter.rus:
        letters = rus_letters
    elif letter == Letter.all:
        letters = string.ascii_letters + string.digits + string.punctuation + rus_letters
    # если ничего из  перечисленного
    else:
        letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    return random.choice(months)


'''
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
'''

'''
def get_random_digits(length):
    digits = string.digits
    return ''.join(random.choice(digits) for i in range(length))
'''


def get_random_phone():
    return "+{}({}){}{}{}-{}{}-{}{}".format(random.randint(1, 9), get_random_string(3, Letter.dig),
                                            *[random.randrange(10) for i in range(7)])


def get_random_email():
    return "{}@{}.{}".format(get_random_string(5), get_random_string(5), get_random_string(2))


def get_random_group():
    # return Group(name=get_random_string(5), header=get_random_string(5), footer=get_random_string(5))
    return Group(name="name-" + get_random_string(10, Letter.eng_rus_dig),
                 footer="footer-" + get_random_string(15, Letter.eng_rus_dig),
                 header="header-" + get_random_string(20, Letter.eng_rus_dig))


def get_random_contact():
    return Contact(lastname=get_random_string(5), firstname=get_random_string(5),
                   middlename=get_random_string(5, Letter.eng_rus_dig), nickname=get_random_string(5),
                   title=get_random_string(10, Letter.all), company=get_random_string(10, Letter.eng_rus_dig),
                   address=get_random_string(10), home=get_random_phone(), mobile=get_random_phone(),
                   work=get_random_phone(), fax=get_random_phone(), email=get_random_email(), email2=get_random_email(),
                   email3=get_random_email(), homepage=get_random_string(10, Letter.eng),
                   bday=str(random.choice(range(1, 31))), bmonth=get_random_month(),
                   byear=random.choice(range(1900, 2024)), aday=str(random.choice(range(1, 31))),
                   amonth=get_random_month(), ayear=random.choice(range(1900, 2024)))
