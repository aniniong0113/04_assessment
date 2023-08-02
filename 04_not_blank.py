# string checker
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print(f"\n {error}. Please try again.\n")
            continue

        return response


while True:
    not_blank("Please enter a string: ", "Cannot be blank")
