import os
from random import randint


def comments(text, name):
    orig_path = os.getcwd()
    os.chdir(f'{os.getcwd()}/comments')
    f = open(f"{name}_comments_{randint(0, 10000)}.txt", 'w+')
    f.write(text)
    f.close()
    os.chdir(orig_path)
