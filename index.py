from Robos import tRobot


def start():
    content = {'SeachTerm': askAndReturnSeachTerm(), 'prefix': askAndReturnPrefix()}
    tRobot.ActivateBootText(content['SeachTerm'])

def askAndReturnSeachTerm():
    return 'Michael Jackson'  # input("Choose a term of Wikipedia: ")


def askAndReturnPrefix():
    menu = {1: 'What is ', 2: 'Who is', 3: 'The history of '}
    for i in menu:
        print(i, ':', menu[i])
    prefix = 2
    # prefix = int(input("Choose one option: "))
    return menu[prefix]


start()
