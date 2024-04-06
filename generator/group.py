import jsonpickle
from model.group import Group
import datahelpers.stringhelper as dh
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


testdata = [Group(name="", footer="", header="")] + [dh.get_random_group() for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    # jsonpickle.set_encoder_options("simplejson", indent=2, ensure_ascii=False, encoding='utf8')
    jsonpickle.set_encoder_options("simplejson", indent=2, encoding='utf8')
    out.write(jsonpickle.encode(testdata))
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
