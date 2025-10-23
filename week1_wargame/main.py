from game_logic.game import init_game, play_round
from utils.deck import create_deck, shuffle


if __name__ == "__main__":
    create_new_deck=create_deck()
    shuffle_deck=shuffle(create_new_deck)
    print(len(shuffle_deck))
    print(shuffle_deck)
#    init_game()
 #  play_round()




#נסיך - J -11
#מלכה - Q -12
#מלך - K -13
#אס - A - 14

#Suits are one of: H, C, D, S.

