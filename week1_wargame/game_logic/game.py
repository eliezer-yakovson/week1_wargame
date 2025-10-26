
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
    player_1["hand"]=deck[:26]
    player_2["hand"]=deck[26:]
    # for i,c in enumerate(deck):
    #     if i<26:
    #         player_1["hand"].append(c)
    #     else:
    #         player_2["hand"].append(c)
    return{"deck":deck, "player_1":player_1, "player_2":player_2}


def play_round(p1: dict, p2: dict) -> str:
    card1 = p1["hand"].pop()
    card2 = p2["hand"].pop()
    result = compare_cards(card1, card2)

    if result == "p1":
        p1["won_pile"] += [card1, card2]
    elif result == "p2":
        p2["won_pile"] += [card1, card2]

    print(f"{p1['name']} drew {card1['rank']}{card1['suite']} ({card1['value']}) | "
          f"{p2['name']} drew {card2['rank']}{card2['suite']} ({card2['value']}) → {result.upper()}")
    return result

