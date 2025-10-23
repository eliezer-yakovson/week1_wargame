import random


def create_card(rank:str,suite:str) -> dict:
    val=0
    if not rank.isnumeric():
        if rank == "J":
            val = 11
        elif rank == "Q":
            val = 12
        elif rank == "K":
            val = 13
        elif rank == "A":
            val = 14
    elif int(rank)>=2 or int(rank) <=10:
        val = int(rank)
    else:
        return{}
    if not suite.isnumeric(): 
        if suite == 'H' or suite == 'C' or suite == 'D' or suite == 'S':
            return {"rank": rank, "suite": suite, "value": val}
    return{}
    
    

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    p1_val=p1_card["value"]
    p2_val=p2_card["value"]
    if p1_val > p2_val:
        return "p1"
    elif p2_card > p1_card:
        return "p2"
    return "WAR"

    return ""
def create_deck() -> list[dict]:
    deck_of_cards=[]
    card_suite_keys={"0":"H", "1":"C" ,"2":"D" ,"3":"S"}
    card_rank_keys={"11":"J", "12":"Q" ,"13":"K" ,"14":"A"}
    for suit in range(4):
        for i in range(2,15):
            if i<11:
                s = card_suite_keys[str(suit)]
                r = str(i)
                cards= create_card(r,s)
                deck_of_cards.append(cards)
            else:
                s = card_suite_keys[str(suit)]
                r = card_rank_keys[str(i)]
                cards= create_card(r,s)
                deck_of_cards.append(cards)
    print (len(deck_of_cards))
    return deck_of_cards

def shuffle(deck:list[dict]) -> list[dict]:
    shuffle_deck = deck.copy()
    for i in range(1000):
        index1 = random.randrange(2,52)
        index2 = random.randrange(2,52)
        if index1 != index2:
            shuffle_deck[index1], shuffle_deck[index2] = shuffle_deck[index2], shuffle_deck[index1]
    return shuffle_deck




        
        


