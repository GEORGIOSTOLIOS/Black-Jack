def initialize_deck():
    kind = {"heart", "diamond", "spade", "club"}
    number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}
    a_deck = {(k, n) for k in kind for n in number}
    return a_deck


deck = initialize_deck()


def player_hand_value(a_card):
    if type(a_card) is int:
        return a_card
    elif a_card == "ace":
        return player_choose_ace_value()
    else:
        return 10


def computer_hand_value(a_card, a_computer_score):
    if type(a_card) is int:
        return a_card
    elif a_card == "ace":
        return computer_choose_ace_value(a_computer_score)
    else:
        return 10


def player_choose_ace_value():
    while True:
        ace_value = input("First, you want the ace card to count as 1 or 11?:")
        if ace_value == "1" or ace_value == "11":
            break
    return int(ace_value)


def computer_choose_ace_value(a_computer_score):
    if a_computer_score + 11 <= 21:
        return 11
    else:
        return 1


def player_calculate_sum(a_player_score, a_card):
    a_player_score += player_hand_value(a_card)
    print(f"The sum of your cards is {a_player_score} ")
    print("-------------------------------")
    return a_player_score


def computer_calculate_sum(a_computer_score, a_card):
    a_computer_score += computer_hand_value(a_card, a_computer_score)
    print(f"The sum of your cards is {a_computer_score} ")
    print("-------------------------------")
    return a_computer_score


def player_lost(a_player_score):
    return a_player_score > 21


def computer_won(a_computer_score, a_player_score):
    return a_player_score <= a_computer_score <= 21


def player_won(a_player_score):
    return a_player_score == 21


def the_winner(computer_score, player_score):
    if player_score > 21:
        return "computer"
    if computer_score > 21:
        return "player"
    winner = "player"
    if computer_score >= player_score:
        winner = "computer"
    return winner


def print_winner(a_winner, winner_score):
    # if the player has lost so the computer did not need to play
    if winner_score == 0:
        print(f"{a_winner} won without playing")
    else:
        print(f"{a_winner} is the winner with score {winner_score}")


def computer_move(a_computer_score, a_player_score):
    print("Computer move:")
    print("")
    # The computer starts with 2 cards
    for i in range(2):
        a_computer_score = computer_draw_card(a_computer_score)

    while True:
        if computer_won(a_computer_score, a_player_score):
            break
        elif a_computer_score < a_player_score:
            print("Would you like to draw again? Yes/No:yes")
            a_computer_score = computer_draw_card(a_computer_score)
            if player_lost(a_computer_score):
                print(f"Computer has score {a_computer_score} so he has lost. ")
                break

    return a_computer_score


def player_move(a_player_score):
    print("Player move:")
    print("")

    # The player starts with 2 cards
    for i in range(2):
        a_player_score = player_draw_card(a_player_score)

    while True:
        if player_won(a_player_score):
            break
        while True:
            choice = input("Would you like to draw again? Yes/No:")
            if choice.lower() == "yes" or choice.lower() == "no":
                break
        if choice.lower() == 'yes':
            a_player_score = player_draw_card(a_player_score)
            if player_lost(a_player_score):
                print(f"Player has score {a_player_score} so he has lost. ")
                break
        else:
            break
    return a_player_score


def player_draw_card(player_score):
    card = deck.pop()
    print(f"The player drew a {card}")
    print("-------------------------------")
    player_score = player_calculate_sum(player_score, card[1])
    return player_score


def computer_draw_card(a_computer_score):
    card = deck.pop()
    print(f"The computer drew a {card}")
    print("-------------------------------")
    computer_score = computer_calculate_sum(a_computer_score, card[1])
    return computer_score


def main():
    player_wins = 0
    computer_wins = 0
    while True:
        player_score = 0
        computer_score = 0
        print_round(computer_wins, player_wins)

        player_score = player_move(player_score)
        if not player_lost(player_score) and not player_won(player_score):
            computer_score = computer_move(computer_score, player_score)

        if the_winner(computer_score, player_score) == "player":
            player_wins += 1
            print_winner("Player", player_score)
        else:
            computer_wins += 1
            print_winner("Computer", computer_score)

        print("-----------------------------------------------------")
        print(f"Score: Player-Computer: {player_wins} - {computer_wins}")
        print("-----------------------------------------------------")

        while True:
            choice = input("Would you like to continue? yes/no:")
            if choice.lower() == "yes" or choice.lower() == "no":
                break
        if choice.lower() == "no":
            break
        else:
            # Repair The deck
            deck.clear()
            a_deck = initialize_deck()
            for i in a_deck:
                deck.add(i)


def print_round(computer_wins, player_wins):
    print("welcome to the game!")
    print("-------------------------------")
    print(f"Round: {player_wins + computer_wins + 1}")
    print("-------------------------------")


main()
