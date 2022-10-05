import inquirer
from random_gen import menu_random
from goodbye import goodbye
from questions import question_list
from data import menu

def user_selections(welcome_answerList):
    questions = [
    inquirer.List('first_question',
                    message="Welcome! Let's find you something to eat",
                    choices=['Yes', 'No', 'Surprise me!'],
                ),
    ]
    answers = inquirer.prompt(questions)
    welcome_answerList.update(answers)
    return welcome_answerList

# next question, processor
# NO => good bye page
# Surprise => random menu generator
def find_user_answer(welcome_answerList):
    final_ans = welcome_answerList['first_question'].lower()
    candidate_menu = []
    # next question, processor
    if final_ans == 'yes':
        #return secondquestion
        question_list()
        
    elif final_ans == 'no':
        #good bye page
        goodbye()
    elif final_ans == 'surprise me!':
        #random menu generator
        menu_random()


def init_welcome():
    welcome_answerList = {}
    user_selections(welcome_answerList)
    find_user_answer(welcome_answerList)
    



