class Deck:
    deck = []
    import random
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    def __init__(self):
     self.deck=deck
     for s in suits:
         for x in range(2, 14):
            self.deck.append(x,s)


    def get_deck(self):
        return self.deck
    def print_deck(self);
        for p in self.deck:
            print(p.get_name())


    def shuffle(self):
        random.shuffle(self.deck)



