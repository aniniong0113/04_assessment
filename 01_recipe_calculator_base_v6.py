# import libs
import pandas
import math


# functions

# round_up
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# not blank checker
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print(f"\n {error}. Please try again.\n")
            continue

        return response


# number checker that checks whether input is a float or
# an integer that is more than zero, takes in custom error messages
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# apply currency
def currency(x):
    return f"${x:.2f}"

# unit converter
def convert_units(value, from_unit, to_unit):
    # Define conversion rates
    conversion_rates = {  # dictionary for conversion rates
        'kg': {'g': 1000, 'mg': 1_000_000, 'l': 1},
        'g': {'kg': 0.001, 'mg': 1000, 'l': 0.001},
        'mg': {'kg': 0.000001, 'g': 0.001, 'l': 0.000001},
        'l': {'kg': 1, 'g': 1000, 'mg': 1_000_000, 'ml': 1000},
        'ml': {'l': 0.001},

    }

    # Check if units are valid
    if from_unit not in conversion_rates or to_unit not in conversion_rates:
        print("Invalid unit!")
        return

    # Perform conversion
    result = value * conversion_rates[from_unit][to_unit]
    return result


def choice_checker(question, choice_list, error):
    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in choice_list:
            if response == var_item:
                return response
            elif response == "y" or response == "n":
                return var_item
        print(error)


# main routine
print("**** Meal Cost Calculator ****\n")

if choice_checker("Would you like to see the instructions?: ",
                  ["yes", "no"],
                  "Please enter either 'yes' or 'no'") == "yes":
    print("\nThis program is relatively straight forward and will ask simple questions which require answers and a "
          "dataframe will be outputted at the end with all needed data.\n")

    # asking whether instructions needed

# getting name of recipe (can't be blank)
meal_name = not_blank("\nWhat is the name of this recipe?: ",
                      "Recipe name must not be blank.")

# getting the amount of servings (must be more than zero)
serving_amount = num_check("How many servings does your recipe make?: ",
                           "Your answer must be larger than 0",
                           float)

# once got serving amount need to get the ingredients,
# amount, cost per ingredient. use loop!!!

# lists for dataframe columns
# ie: for food, ingredients, amount needed, price per amount, etc.
recipe_amount = []
recipe_amount_unit = []
ingredients = []
ingredient_amount_bought = []
ingredient_price_per_amount_bought = []
ingredient_unit_per_amount_bought = []
cost_to_make = []
cost_to_make_numbers = []

# recipe ingredients dictionary for recipe ingredients dataframe
recipe_ingredients = {
    "Amount": recipe_amount,
    "Unit": recipe_amount_unit,
    "Ingredients": ingredients
}

ingredient_price = {  # ingredient price table
    "Price": ingredient_price_per_amount_bought,
    "Ingredients": ingredients,
    "Amount": ingredient_amount_bought,
    "Unit": ingredient_unit_per_amount_bought,
    "Cost to make": cost_to_make
}

ingredient_count = num_check("How many ingredients are in your recipe?: ",
                             "Must be an integer greater than 0",
                             int)  # amount of ingredients for loop

ingredients_len = len(ingredients)  # get count of ingredients

print("\n**** Recipe Ingredients and Ingredient Prices ****\n")

while ingredients_len <= (ingredient_count - 1):  # loop for ingredient names, unit, amount
    ingredient_to_append = not_blank("Please enter ingredient name: ",
                                     "Ingredient name cannot be blank")
    recipe_unit_to_append = choice_checker("What unit do you measure this ingredient with in the recipe?"
                                           " (if it is counted please enter count): ",
                                           ["kg", "g", "mg", "l", "ml", "count"],
                                           "Please enter one of the choices: kg, g, mg, l, ml, count")
    recipe_amount_unit.append(recipe_unit_to_append)  # append recipe unit to list in respect to order of ingredients
    ingredients.append(ingredient_to_append)  # adds ingredient name to list
    ingredients_len = ingredients_len + 1  # adds 1 to the length for each ingredient unit for looping purpose
    # gets the unit and amount to append to the list for the database later on
    if recipe_unit_to_append == "count":
        recipe_amount_to_append = num_check(f"How many are you using?: ",  # getting amount used in recipe
                                            "Please enter a number greater than 0, no characters",
                                            float)
    else:
        recipe_amount_to_append = num_check(f"How many {recipe_unit_to_append} are you using?: ",
                                            "Please enter a number greater than 0, no characters",
                                            float)
    # appends the recipe amount
    recipe_amount.append(recipe_amount_to_append)
    print()
    # if the recipe unit is count then the bought unit is automatically count because you
    # cannot convert from weight to count
    if recipe_unit_to_append == "count":
        bought_unit_to_append = "count"
        pass
    else: # takes a multichoice input for what unit the ingredient was measured in
        bought_unit_to_append = choice_checker(f"What unit was {ingredient_to_append} measured in when you bought it?",
                                               ["kg", "g", "mg", "l", "ml"],
                                               "Please enter one of the choices: kg, g, mg, l, ml")
    # appending unit for bought amounts
    ingredient_unit_per_amount_bought.append(bought_unit_to_append)
    # if the bought unit was count then it asks how many they bought
    if bought_unit_to_append == "count":
        bought_amount_to_append = num_check(f"How many did you buy?: ",  # getting amount bought
                                            "Please enter a number greater than 0, no characters",
                                            float)
    else: # gets the amount of unit they bought
        bought_amount_to_append = num_check(f"How many {bought_unit_to_append} did you buy?: ",
                                            "Please enter a number greater than 0, no characters",
                                            float)
    ingredient_amount_bought.append(bought_amount_to_append)
    # above line appends bought amount
    # gets how much they paid for the amount they bought
    if bought_unit_to_append == "count":
        ingredient_price_per_amount_bought_to_append = num_check(
            f"How much did you pay for {bought_amount_to_append}?: $",
            "please enter a number greater than 0",
            float)
    else:
        ingredient_price_per_amount_bought_to_append = num_check(
            f"How much did you pay for {bought_amount_to_append}{bought_unit_to_append}?: $ ",
            "please enter a number greater than 0",
            float)
    # appends the price to list
    ingredient_price_per_amount_bought.append(currency(ingredient_price_per_amount_bought_to_append))

    # *** Cost to smake below *** #
    if recipe_unit_to_append == bought_unit_to_append:
        converted_amount = recipe_amount_to_append
    else:
        converted_amount = convert_units(recipe_amount_to_append,
                                         recipe_unit_to_append,
                                         bought_unit_to_append)
    # calculating the cost to make
    cost_to_make_to_append = converted_amount * (ingredient_price_per_amount_bought_to_append / bought_amount_to_append)
    cost_to_make.append(currency(cost_to_make_to_append))
    # appends cost to make to append so that calculate total at the end
    cost_to_make_numbers.append(cost_to_make_to_append)
    print()
# printing the dataframes and formatting it
print("\n\n**** ---- **** Recipe Ingredients **** ---- ****\n")
recipe_ingredients_frame = pandas.DataFrame(recipe_ingredients)
recipe_ingredients_frame = recipe_ingredients_frame.set_index("Amount")
print(recipe_ingredients_frame)

print("\n\n**** ---- **** Ingredient Prices **** ---- ****\n")
ingredient_price_frame = pandas.DataFrame(ingredient_price)
ingredient_price_frame = ingredient_price_frame.set_index("Price")
print(ingredient_price_frame)

# get total price and print it

total = sum(cost_to_make_numbers)
print()
print(f"Total Cost:{currency(total)}")
print(f"Per Serving: {currency(total / serving_amount)}")
print()
