def choice_checker(question, choice_list, error):
    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in choice_list:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        print(error)


while True:
    choice_checker(
        "Please enter yes or no: ",
        ["yes", "no"],
        "Please enter yes or no (whole word)"
    )
