if [[ $# -eq 1 ]]; then
    
    if [[ "$1" == "run" ]]; then
        echo "Start main_app.py"
        python3 main_app.py
    fi
     if [[ "$1" == "help" ]]; then
        echo "There are several package you need to install before runing this app."
        echo "pip install inquirer or pip3 install inquirer"
    fi
    if [[ "$1" == "how" ]]; then
        echo "- There are set of questions to find the right dish for you"
        echo "- Use arrow to navigate the options"
        echo "- If you select 'surprise me' you can have a randomised menu item chosen for you."
    fi
else 
    echo "No parameter"
fi
