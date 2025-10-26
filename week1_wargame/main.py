from game_logic.game import init_game, play_round
   

if __name__ == "__main__":
    game = init_game()
    p1 = game["player_1"]
    p2 = game["player_2"]

    for i in range(10):
        print(f"\n------------------- Round {i+1} -------------------")
        if not p1["hand"] or not p2["hand"]:
            print("Game Over! One player ran out of cards.")
            break

        print(f"{p1['name']}: hand={len(p1['hand'])}, won={len(p1['won_pile'])}")
        print(f"{p2['name']}: hand={len(p2['hand'])}, won={len(p2['won_pile'])}")
        play_round(p1, p2)

    print("\n------------------- Final Results -------------------")
    p1_wins = len(p1["won_pile"])
    p2_wins = len(p2["won_pile"])
    if p1_wins > p2_wins:
        print(f"🏆 {p1['name']} Wins with {p1_wins} cards!")
    elif p2_wins > p1_wins:
        print(f"🏆 {p2['name']} Wins with {p2_wins} cards!")
    else:
        print("It's a draw!")



  
