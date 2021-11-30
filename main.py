# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from art import logo
import random

user_cards = []
dealer_cards = []
user_score = 0
dealer_score = 0
is_game_on = True


# Step 1: Create a deal_card() function that uses the List below to *return* a random card. 11 is the Ace.


def deal_card(player_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    if random_card == 11:
        if sum(player_cards) > 10:
            random_card = 1
    return random_card


# Step 2: Deal the user and computer 2 cards each using deal_card() and append().

for i in range(2):
    user_cards.append(deal_card(user_cards))
    dealer_cards.append(deal_card(dealer_score))


# Step 3: Create a function called calculate_score() that takes a List of cards as input and returns the score.


def calculate_score(player_cards):
    return sum(player_cards)


# Step 7: Create a function called compare() and pass in the user_score and computer_score.
# If the user_score is over 21, then the user loses.
# If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.
# If the computer and user both have the same score, then it's a draw.
def compare(player_score,  computer_score):
    if player_score > 21:
        print("You Lose.")
    elif computer_score > 21:
        print("You Win.")
    else:
        if player_score > computer_score:
            print("You Win.")
        elif player_score < computer_score:
            print("You Lose.")
        else:
            print("It's a draw.")


print(logo)
print(f"Your Cards: {user_cards}, your score is {calculate_score(user_cards)}")
print(f"Computer's first card: {dealer_cards[0]}")

while is_game_on:
    # Step 4: Ask the user if they want to draw another card.
    # If yes, then use the deal_card() function to add another card to the user_cards List.
    # If no, then the game has ended.
    user_choice = input("Type 'y' to get another card or 'n' to pass.").lower()
    if user_choice == 'y':
        user_cards.append(deal_card(user_cards))
        print(f"Your hands: {user_cards}, your score is {calculate_score(user_cards)}")
        print(f"Computer's hands: {dealer_cards}")
        user_score = calculate_score(user_cards)
        # Step 5: The score will need to be rechecked with every new card drawn and
        # need to be repeated until the game ends.
        if user_score > 21:
            print("You Lose.")
            is_game_on = False

    elif user_choice == 'n':
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        # Step 6: Once the user is done, it's time to let the computer play.
        # The computer should keep drawing cards as long as it has a score less than 17.
        while dealer_score < 17:
            dealer_cards.append(deal_card(dealer_cards))
            dealer_score = calculate_score(dealer_cards)

        print(f"Your final hands: {user_cards}")
        print(f"Computer's final hands: {dealer_cards}")
        compare(user_score, dealer_score)
        is_game_on = False



