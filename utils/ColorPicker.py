import random

def get_rand_color():
    de = ("%02x" % random.randint(0, 255))
    re = ("%02x" % random.randint(0, 255))
    we = ("%02x" % random.randint(0, 255))
    ge = "#"
    color = ge + de + re + we

    return color