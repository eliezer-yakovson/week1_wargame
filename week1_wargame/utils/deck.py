import random

def create_card(rank: str, suite: str) -> dict:
    valid_suites = {'H', 'C', 'D', 'S'}
    if suite not in valid_suites:
        return {}

    if rank.isnumeric():
        val = int(rank)
        if 2 <= val <= 10:
            return {"rank": rank, "suite": suite, "value": val}
    elif rank in {'J', 'Q', 'K', 'A'}:
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[rank]
        return {"rank": rank, "suite": suite, "value": val}
    return {}



def compare_cards(p1_card:dict, p2_card:dict) -> str:
    p1_val=p1_card["value"]
    p2_val=p2_card["value"]
    if p1_val > p2_val:
        return "p1"
    elif p1_val < p2_val:
        return "p2"
    return "WAR"

    return ""


def create_deck() -> list[dict]:
    ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suites = ['H', 'C', 'D', 'S']
    deck = [create_card(r, s) for s in suites for r in ranks]
    return deck


def shuffle(deck:list[dict]) -> list[dict]:
    shuffle_deck = deck.copy()
    for i in range(1000):
        index1 = random.randrange(2,52)
        index2 = random.randrange(2,52)
        if index1 != index2:
            shuffle_deck[index1], shuffle_deck[index2] = shuffle_deck[index2], shuffle_deck[index1]
    return shuffle_deck

# def shuffle(deck: list[dict]) -> list[dict]:
#     shuffled = deck.copy()
#     random.shuffle(shuffled)
#     return shuffled





        
        


