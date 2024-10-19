import random

def start_game():
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11)) + ["+2"]  # Add "+2" as a special rank
    deck = [(rank, colour) for rank in ranks for colour in colours]
    random.shuffle(deck)

    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]

    central_card = deck.pop(0)
    main_loop(p1, p2, deck, central_card, 0)



def main_loop(p1, p2, deck, central_card, whose_turn):
    while len(p1)>0 and len(p2)>0:
        print(f"\nPlayer {whose_turn + 1}'s turn, here is your hand {p1}")
        print(f"Central card is: {central_card}")


        ans = int(input("You have a choice. You can (0) draw or (1) play: "))
        if ans == 1:
            valid_play_found = "No :("
            
        while valid_play_found == "No :(":
            player_choice = int(input("Which card to play? (Enter the card number starting from 1): ")) - 1
            if 0 <= player_choice < len(p1):
                valid = valid_play(central_card, p1[player_choice])
                if valid:
                    central_card = p1.pop(player_choice)
                    valid_play_found = "Yup"
                else:
                    print("Invalid play. Please choose a valid card.")
            else:
                print("Invalid card selection. Please try again.")

        plus2_flag = True
        if central_card[0] == "+2" and plus2_flag==True:
            print("The opponent must draw 2 cards!")
            p2.append(deck.pop(0))
            p2.append(deck.pop(0))
            plus2_flag = False

        elif ans == 0:
            draw_card = deck.pop(0)
            p1.append(draw_card)

        p1, p2 = p2, p1
        whose_turn = (whose_turn + 1) % 2




def valid_play(card1, card2):
    return card1[0] == card2[0] or card1[1] == card2[1]

start_game()
