import random
from data import menu

def menu_random():
    print("Be adventrous and find or make:", random.choice(list(menu.keys())))
    return random.choice(list(menu.keys()))