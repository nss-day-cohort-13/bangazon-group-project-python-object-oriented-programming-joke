def prompt(message):
    """
    Prompt the user for input

    Arguments:
        message     the message used in the prompt

    Returns:
        the entered value
    """

    print('\n' + message)
    return input('> ')

def show_menu(heading, menu_dict, prompt_message):
    """
    Get a menu selection from the user

    Arguments:
        heading         a heading to show for the menu
        menu_dict       the menu of options and values
        prompt_message  a message to use as a prompt

    Returns:
        the matched value from the menu
    """

    key_matches = []
    while len(key_matches) != 1:
        print('\n' + heading)
        [print(key) for key in sorted(menu_dict.keys())]
        choice = prompt(prompt_message)

        key_matches = [key for key in menu_dict.keys()
                        if choice.lower() in key.lower()]

        if len(key_matches) == 0: print('\n-- No matches found.')
        if len(key_matches) > 1: print('\n-- Too many matches found.')

    return menu_dict[key_matches[0]]


if __name__ == '__main__':
    num = -1
    while num:
        num = show_menu('Heading Test',
                        {'1. one': 1, '2. two':2, '3. three':3, 'Exit':None},
                        'Choose a number')
        if num: print('\n-- You chose ' + str(num))
