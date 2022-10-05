import random_gen


def test_randg():
    firstAns = str(random_gen.menu_random())
    secondAns = str(random_gen.menu_random())
    thirdAns = str(random_gen.menu_random())
    
    if firstAns == secondAns and secondAns == thirdAns:
        print("Error")
    else:
        print("Test passed")

test_randg()

