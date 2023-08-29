import random
from card import Card

class Deck:


    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    def __init__(self):
     self.deck=[]
     for s in Deck.suits:
         for x in range(2, 14):
            self.deck.append(Card(x,s))


    def get_deck(self):
        return self.deck

    def print_deck(self):
        for p in self.deck:
            print(p.get_name())


    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)

if __name__ == '__main__':
    shoot1=Deck()
    # print(print_deck)



