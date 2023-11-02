import math
import random


def gen_code():
    digits = "0123456789"
    code = ""
    for i in range(6):
        code += digits[math.floor(random.random() * 10)]
    return code