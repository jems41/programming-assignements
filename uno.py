# code by David Hack and James Combista
# implemented +2 and Skip Turn

import random


def start_game():
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11)) + ["+2"] + ["Skip Turn"]  # Add "+2" and Skip Turn as special ranks
    deck = [(rank, colour) for rank in ranks for colour in colours]
    random.shuffle(deck)

    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]

    central_card = deck.pop(0)
    main_loop(p1, p2, deck, central_card, 0)


def main_loop(p1, p2, deck, central_card, whose_turn):
    count = 0
    while len(p1) > 0 and len(p2) > 0:

        print(f"\nPlayer {whose_turn + 1}'s turn, here is your hand {p1}")
        print(f"Central card is: {central_card}")


        ans = int(input("You have a choice. You can (0) draw or (1) play: "))
        if ans != 1 and ans != 0:
            for _ in range(100):
                ans = int(input("Bad Choice. You can (0) draw or (1) play: "))
                if ans == 1 or ans == 0:
                    break
        skip_turn = True
        if ans == 1:
            valid_play_found = "No :("

            while valid_play_found == "No :(":
                player_choice = int(input("Which card to play? (Enter the card number starting from 1): ")) - 1
                if 0 <= player_choice < len(p1):
                    valid = valid_play(central_card, p1[player_choice])
                    if valid:
                        player_card = p1[player_choice]
                        central_card = p1.pop(player_choice)
                        valid_play_found = "Yup"
                    else:
                        print("Invalid play. Please choose a valid card.")
                else:
                    print("Invalid card selection. Please try again.")

# +2 card code

            if ((player_card)[0]) == "+2":
                print("The opponent must draw 2 cards!")
                p2.append(deck.pop(0))
                p2.append(deck.pop(0))

# Skip turn card code ->
        
            if central_card[0] == "Skip Turn" and skip_turn == True:
                print("The opponent turn has been skipped!")
                whose_turn = (whose_turn + 1)
                skip_turn = False
                count += 1

        elif ans == 0:
            draw_card = deck.pop(0)
            p1.append(draw_card)

        if skip_turn:
            p1, p2 = p2, p1

        count += 1

        whose_turn = (whose_turn + 1) % 2

# Determining winner code
    if count % 2 == 0:
        print(f"Player 2 wins")
    else:
        print("Player 1 wins!!!1")

def valid_play(card1, card2):
    return card1[0] == card2[0] or card1[1] == card2[1]

start_game()
