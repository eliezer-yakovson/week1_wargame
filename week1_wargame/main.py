from game_logic.game import init_game, play_round
from utils.deck import create_deck, shuffle


if __name__ == "__main__":
    int_g = init_game()
    for i in range(10):
        print("-------------------------",i,"------------------------------")
        print("------player1---------")
        print(int_g["player_1"]["name"], end=" ")
        print(len(int_g["player_1"]["hand"]), end=" ")
        print(len(int_g["player_1"]["won_pile"]))
        print("------player2----------")
        print(int_g["player_2"]["name"], end=" ")
        print(len(int_g["player_2"]["hand"]), end=" ")
        print(len(int_g["player_2"]["won_pile"]))
        play_round(int_g["player_1"],int_g["player_2"])
        

    

    print()



  
