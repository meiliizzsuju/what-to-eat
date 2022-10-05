import inquirer
from data import menu
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

def question_0(answerList):
    questions = [
      inquirer.List('geo_question',
                    message="Okay let's choose an origin",
                    choices=['south asian', 'europe', 'south america', 'east asian', 'eastern europe', 'north america'],
                ),
    ]
    questions0_answers = inquirer.prompt(questions)
    answerList.update(questions0_answers)
    return answerList

def question_1(answerList):
    questions = [
      inquirer.List('first_question',
                    message="Okay let's choose a base",
                    choices=['rice', 'soup', 'noodle', 'bread','none'],
                ),
    ]
    questions1_answers = inquirer.prompt(questions)
    answerList.update(questions1_answers)
    return answerList

def question_2(answerList):
    questions = [
      inquirer.List('second_question',
                    message="Okay let's choose a protein",
                    choices=['chicken','seafood','beef', 'pork', 'vegetarian'],
                ),
    ]
    questions2_answers = inquirer.prompt(questions)
    answerList.update(questions2_answers)
    return answerList
  
def question_3(answerList):
    questions = [
      inquirer.List('third_question',
                    message="Now, do you have any allergies?",
                    choices=['nut', 'dairy', 'gluten', 'meat', 'seafood', 'none'],
                ),
    ]
    questions3_answers = inquirer.prompt(questions)
    answerList.update(questions3_answers)
    return answerList


def resultDisplay(result):
  if len(result) > 0:
    print("You can go and grab...")
    for final_ans in result:

      print("=>", final_ans)
  else:
    print("Sorry, we can't find your match")

def findthecandidate(ansList):
    geo_candidate_list = []
    subcat_list = []
    candidate_list = []

    for ans in ansList: # loop the  anwers that we got
      if ans == 'geo_question':
        for g in menu:
          geo_value = menu[g]['main_category']

          if geo_value == ansList[ans]:
            if len(geo_candidate_list) == 0: # check if there is any thing on the list
                geo_candidate_list.append(g)
            elif len(geo_candidate_list) > 0: # if the list is not empty, just add the new found item
              if g not in geo_candidate_list:
                geo_candidate_list.append(g)

      # Find by sub_category
      if ans == 'first_question':
          for sub_item in menu:
            sub_value = menu[sub_item]['sub_category']
            for selected_geo in geo_candidate_list:
              if sub_item == selected_geo:
                  base_list = sub_value.split(', ')
                  for base in base_list:

                    
                    if base == ansList[ans]:
                      if len(subcat_list) == 0: # check if there is any thing on the list
                        subcat_list.append(sub_item)
                      elif len(subcat_list) > 0: # if the list is not empty, just add the new found item
                        if sub_item not in subcat_list:
                          subcat_list.append(sub_item)


      # find by proteins
      if ans == 'second_question': # we know that first and second question are looking for protein
        # loop from the slected GEO list
        # print("when this?")
        for item in menu:
          for selected_geo in subcat_list:
            if item == selected_geo: # when item in the menu matched with selected 'main_category'
              # print("selected_geo : ",selected_geo)
              # for k in menu:
              protein_list = menu[item]['protein'].split(', ') #split the proteins by ', ' and make it a list
              for intg_item in protein_list: # looping trough the ingredent list
                checkCloseMatch = len(get_close_matches(ansList[ans], protein_list, 5, 0.6))
                if (checkCloseMatch > 0) or intg_item == ansList[ans]: # then check if any of the asnwer match ingredeints
                  if len(candidate_list) == 0: # check if there is any thing on the list
                    candidate_list.append(item)
                  elif len(candidate_list) > 0: # if the list is not empty, just add the new found item
                    if item not in candidate_list:
                      candidate_list.append(item)
                
    # remove if there is allergy set in the anwer
    for menu_item in candidate_list:
      allergy_list = menu[menu_item]['allergies'].split(', ')
      for allergy in allergy_list:
          if allergy == ansList['third_question']:
            candidate_list.remove(menu_item)


            

    # check the candidate list

    resultDisplay(candidate_list)
                


def question_list():
  answerList = {}
  question_0(answerList)
  question_1(answerList)
  question_2(answerList)
  question_3(answerList)

  findthecandidate(answerList)

