# Dependancies

The application requires the user have  inquirerer package installed on their computer. 

``` pip install inquirer or pip3 install inquirer ```




# Usage

To begin running the app, run ```python3 main_app.py```  or ```./run_what_to_eat.sh run``` in the terminal.

1. Selection Process 
    Selection process is named 'Selections' in the application, and as explained above, is a feature that filters user choices and returns a menu item by comparing the dictionary of menu items. The user must go through and pick answers from five questions:

Let's find something to eat?:

    1. confirm that you wish to find menu item based on preferences by picking 'yes'.
    2. confirm that you do not wish to do so by picking 'no'
    3. pick 'Surpirse me!' if you would rather find menu item at random

Choose an Origin:
         
    pick a preference by geography i.e. south asian.

Choose a base:
         
    pick a preference by geography i.e. rice.

Choose Protein

         pick a preference by protien  i.e. chicken.

Any Allergies

        pick to remove any category of allergy  i.e. seafood.

2. Lookup feature for the ingredients in a menu 

        At the start of the application, pick 'Menu Item Ingredient'.
        Then type the desired Menu item to view list of ingredients.

3. Random generator 

        pick the 'Surprise me!' option in the beginning of the Selection stage.
