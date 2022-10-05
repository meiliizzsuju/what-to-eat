from data import menu
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
import homepage 

keys = menu.keys()


def get_menu(word):
    word = word.title()
    if word in menu or len(get_close_matches(word, keys)) > 0:
        if len(get_close_matches(word, keys)) > 0:
            user_input = input("Did you mean %s ? Enter Y for Yes, or N for No: " % get_close_matches(word, menu.keys())[0])
            user_input = user_input.upper()
            if user_input == "Y":
                search_result = menu[get_close_matches(word, menu.keys())[0]]
                print("Ingredient for ",word," are ...")
                print (search_result['ingredient'])
                print("Bon Appétit !!!")
            elif user_input == "N":
                homepage.init_main_page()

    else:
        print('unknown menu item, please try again.')
        init_get_menu()
    


def init_get_menu():
    menu_item = input('What menu item do you want to check ingredients? ex. Pho, Hamburger:')
    get_menu (menu_item)
    


