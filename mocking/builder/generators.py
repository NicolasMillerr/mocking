import string
import random


def make_string(length: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
