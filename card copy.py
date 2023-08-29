class Card:
    names=["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__ (self):
        return f"value: {self.value}, {self.suit} "

    def get_name(self):
        return f"{Card.names[self.value-2]} of {self.suit}"

    def image_file_name(self):
        if self.value <= 10:
            return f"{self.value}_of_{self.suit.lower()}.png"
        else:
            return f"{Card.names[self.value-2].lower()}_of_{self.suit.lower()}.png"


if __name__ == '__main__':
    card1 = Card(2, "Spades")
    print(card1.get_name())

