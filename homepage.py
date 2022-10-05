import inquirer
from app import init_get_menu
from welcome import init_welcome
from goodbye import goodbye

def search_user_answer(user_ans):
  user_ans = user_ans['home_page'].lower()
  if user_ans == 'selections':
    init_welcome()
  elif user_ans == 'menu item ingredients':
    init_get_menu()
  elif user_ans == 'exit':
    goodbye()


def init_main_page():
  home_questions = [
  inquirer.List('home_page',
                message="Welcome! Let's find you something to eat",
                choices=['Selections', 'Menu Item Ingredients', 'Exit'],
            ),
  ]
  answers_home = inquirer.prompt(home_questions)

  search_user_answer(answers_home)
