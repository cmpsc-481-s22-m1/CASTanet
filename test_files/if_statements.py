"""A file to test if statements."""


def blackjack():
    """Play blackjack with the user."""
    dealer_hand = 20
    my_hand = 18
    my_bet = 2
    my_account = 120

    if dealer_hand > my_hand:
        #Dealer wins
        my_account -= my_bet

    if dealer_hand < my_hand:
        #Dealer loses
        my_account += my_bet

    if my_hand == 21:
        #Blackjack doubles wins
        my_account += (my_bet*2)

    if my_account < my_bet:
        print("Do not have enough funds to cover this amount")
        if my_account <= 0:
            print("Your account is empty")
