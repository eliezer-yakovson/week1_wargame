
from utils.deck import compare_cards, create_deck, shuffle


def create_player(name:str) -> dict:
    if name:
        return {"name":name,"hand":[],"won_pile":[]}
    else:
        return {"name":"AI","hand":[],"won_pile":[]}

def init_game()->dict:
    first_deck = create_deck()
    deck = shuffle(first_deck)
    print("enter tha name")
    p1 = input()
    player_1 = create_player(p1)
    player_2 = create_player("")
    for i,c in enumerate(deck):
        if i<26:
            player_1["hand"].append(c)
        else:
            player_2["hand"].append(c)

    return{"deck":deck, "player_1":player_1, "player_2":player_2}

def play_round(p1:dict,p2:dict):
    player_1=p1["hand"].pop()
    player_2=p2["hand"].pop()
    bigger = compare_cards(player_1,player_2)
    if bigger =="p1":
        p1["won_pile"].append(player_1)
        p1["won_pile"].append(player_2)
    elif bigger =="p2":
        p2["won_pile"].append(player_1)
        p2["won_pile"].append(player_2)
    print(player_1["value"], end = "===")
    print(player_2["value"])
