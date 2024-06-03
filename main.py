###############################################################################
# Yu-Gi-Oh! Card Data Analysis
# Pseudo Code for Main Algorithm
#   Prompt the user to input the file name.
#   Prompt the user to input the option.
#   A while loop to check the user's input.
#       If the user's input is 1, display the number of cards in the dataset
#          and display the first 50 cards.
#       If the user's input is 2, prompt the user to input the query and
#          the category to search. Then, display the search results.
#       If the user's input is 3, prompt the user to input the decklist file name.
#       If the user's input is 4, display a message and break the loop.
#       Else, display an error message and prompt the user to input again.
###############################################################################


# import the csv module and the itemgetter function from the operator module
import csv
from operator import itemgetter

# Strings that will use in the program
"\nFile not Found. Please try again!"

"{'Name'}{'Type'}{'Race'}{'Archetype'}{'TCGPlayer'}"
"{}{}{}{}{}"
"\n{'Totals'}{''}{''}{''}{}"

"\nThe price of the least expensive card(s) is {}"
"\nThe price of the most expensive card(s) is {}"
"\nThe price of the median card(s) is {}"
"\t{}" #display the cards after the search

"\nInvalid option. Please try again!"
"\nEnter cards file name: "
"\nThere are {} cards in the dataset."
"\nEnter query: "
"\nEnter category to search: "
"\nIncorrect category was selected!"
"\nSearch results"
"\nThere are {} cards with '{}' in the '{}' category."
"\nThere are no cards with '{}' in the '{}' category."
"\nEnter decklist filename: "
"\nThanks for your support in Yu-Gi-Oh! TCG"

MENU = "\nYu-Gi-Oh! Card Data Analysis" \
           "\n1) Check All Cards" \
           "\n2) Search Cards" \
           "\n3) View Decklist" \
           "\n4) Exit" \
           "\nEnter option: "

CATEGORIES = ["id", "name", "type", "desc", "race", "archetype", "card price"]

def open_file(prompt_str):
    """
    This function will prompt the user to input the file name and open the file.
    Value: prompt_str (str)
    Return: fp (file pointer
    """

    # A while loop to check the user's input
    while True:
        try:
            file_name = input(prompt_str)
            fp = open(file_name, "r", encoding="utf-8")
            return fp
        except FileNotFoundError:
            print("\nFile not Found. Please try again!")

def read_card_data(fp):
    """
    This function will read the card data from the file and return a list of tuples
    sorted by card price and name.
    Value: fp (file pointer)
    Return: sorted_card_data (list of tuples)
    """
    card_data = []

    # Read the file and append the card data to the list
    reader = csv.reader(fp, delimiter=",")

    # Skip the header
    next(reader, None)

    for line in reader:
        card_data.append((line[0], line[1][:45], line[2], line[3], line[4], line[5], float(line[6])))

    # Sort the card data by card price and name
    sorted_card_data = sorted(card_data, key=itemgetter(6, 1))
    return sorted_card_data

def search_cards(card_data, query, category_index):
    """
    This function will search the cards that match the query and return a list of tuples.
    Value: card_data (list of tuples), query (str), category_index (int)
    Return: result_list (list of tuples)
    """
    result_list = []
    for i in range(len(card_data)):
        if query in card_data[i][category_index]:
            result_list.append(card_data[i])
    return result_list

def read_decklist(fp, card_data):
    """
    This function will read the decklist from the file and return a list of tuples
    sorted by card price and name.
    Value: fp (file pointer), card_data (list of tuples)
    Return: sorted_a_list (list of tuples)
    """
    a_list = []
    for line in fp:
        for j in range(len(card_data)):
            if line.strip() == card_data[j][0]:
                a_list.append(card_data[j])

    # Sort the decklist by card price and name
    sorted_a_list = sorted(a_list, key=itemgetter(6, 1))
    return sorted_a_list


def compute_stats(card_data):
    """
    This function will compute the minimum, maximum, and median card prices and return
    the list of tuples for each category.
    Value: card_data (list of tuples)
    Return: sorted_min_list (list of tuples), min_price (float), sorted_max_list (list of tuples),
            max_price (float), sorted_med_list (list of tuples), med_price (float)
    """

    # Initialize the minimum and maximum prices
    min_price = 1000000
    max_price = -1

    # Create empty lists for the minimum, maximum, and median card prices
    min_list = []
    max_list = []
    med_list = []
    for i in range(len(card_data)):
        if float(card_data[i][6]) > max_price:
            max_price = float(card_data[i][6])
        if float(card_data[i][6]) < min_price:
            min_price = float(card_data[i][6])

    sorted_card_data = sorted(card_data, key=itemgetter(6))

    # Compute the median price
    if len(sorted_card_data) % 2 == 0:
        med_price = max(float(sorted_card_data[len(sorted_card_data) // 2][6]) , float(sorted_card_data[(len(sorted_card_data) // 2) - 1][6]))
    else:
        med_price = float(sorted_card_data[len(sorted_card_data) // 2][6])

    # Append the cards to the minimum, maximum, and median lists
    for i in range(len(card_data)):
        if float(card_data[i][6]) == min_price:
            min_list.append(card_data[i])
        if float(card_data[i][6]) == max_price:
            max_list.append(card_data[i])
        if float(card_data[i][6]) == med_price:
            med_list.append(card_data[i])

    # Sort the minimum, maximum, and median lists by card name
    sorted_min_list = sorted(min_list, key=itemgetter(1))
    sorted_max_list = sorted(max_list, key=itemgetter(1))
    sorted_med_list = sorted(med_list, key=itemgetter(1))

    return sorted_min_list, min_price, sorted_max_list, max_price, sorted_med_list, med_price

def display_data(card_data, n="use card length"):
    """
    This function will display the card data and the total price.
    Value: card_data (list of tuples), n (int)
    Return: None
    """
    total_price = 0
    print(f"{'Name':<50}{'Type':<30}{'Race':<20}{'Archetype':<40}{'TCGPlayer':<12}")

    # Use the default value of n if the user does not input the value
    # In the main part, when we recall this function, we can set n = 50 to display the first 50 cards

    if n == "use card length":
        n = len(card_data)
    else:
        n = n

    # Display the card data and the total price
    for i in range(n):
        print(f"{card_data[i][1]:<50}{card_data[i][2]:<30}{card_data[i][4]:<20}{card_data[i][5]:<40}{card_data[i][6]:>12,.2f}")
        total_price += float(card_data[i][6])
    print(f"\n{'Totals':<50}{'':<30}{'':<20}{'':<40}{total_price:>12,.2f}")



def display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price):
    """
    This function will display the minimum, maximum, and median card prices.
    Value: min_cards (list of tuples), min_price (float), max_cards (list of tuples),
           max_price (float), med_cards (list of tuples), med_price (float)
    Return: None
    """
    print(f"\nThe price of the least expensive card(s) is {min_price:,.2f}")
    for card in min_cards:
        print(f"\t{card[1]}")
    print(f"\nThe price of the most expensive card(s) is {max_price:,.2f}")
    for card in max_cards:
        print(f"\t{card[1]}")
    print(f"\nThe price of the median card(s) is {med_price:,.2f}")
    for card in med_cards:
        print(f"\t{card[1]}")



def main():
    """
    This function will prompt the user to input the file name and the option.
    Value: None
    Return: None
    """

    prompt_str = "\nEnter cards file name: "

    # Open the file and read the card data
    fp = open_file(prompt_str)
    card_data = read_card_data(fp)

    # Prompt the user to input the option
    user_option = input(MENU)

    # A while loop to check the user's input
    while True:
        if user_option == '1':

            print(f"\nThere are {len(card_data)} cards in the dataset.")

            # Display the first 50 cards
            display_data(card_data, n=50)

            min_cards, min_price, max_cards, max_price, med_cards, med_price = compute_stats(card_data)
            display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price)

            user_option = input(MENU)

        elif user_option == '2':
            user_input_query = input("\nEnter query: ")
            while True:

                user_input_category = (input("\nEnter category to search: ")).lower()
                if user_input_category in CATEGORIES:


                    category_index = CATEGORIES.index(user_input_category)
                    result_list = search_cards(card_data, user_input_query, category_index)

                    # Display the search results when there is result_list
                    if len(result_list) > 0:
                        print(f"\nSearch results")
                        print(f"\nThere are {len(result_list)} cards with '{user_input_query}' in the '{user_input_category}' category.")
                        display_data(result_list)

                        min_cards, min_price, max_cards, max_price, med_cards, med_price = compute_stats(result_list)
                        display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price)

                    else:
                        print(f"\nSearch results")
                        print(f"\nThere are no cards with '{user_input_query}' in the '{user_input_category}' category.")

                    break
                else:
                    print("\nIncorrect category was selected!")

            user_option = input(MENU)

        elif user_option == '3':

            # Open the file and read the decklist
            prompt_str = input("\nEnter decklist filename: ")

            # Open the ydk file and read the decklist
            fp_ydk = open(prompt_str, "r", encoding="utf-8")

            print(f"\nSearch results")

            decklist = read_decklist(fp_ydk, card_data)

            display_data(decklist)

            min_cards, min_price, max_cards, max_price, med_cards, med_price = compute_stats(decklist)
            display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price)

            user_option = input(MENU)

        elif user_option == '4':
            print("\nThanks for your support in Yu-Gi-Oh! TCG")
            break

        else:
            print("\nInvalid option. Please try again!")
            user_option = input(MENU)


if __name__ == "__main__":
    main()