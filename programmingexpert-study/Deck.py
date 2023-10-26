class Deck:
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    suits = ["D", "H", "C", "S"]  # Diamond, Heart, Club, Spade

    def __init__(self):
        self.deck = []
        self.fill_deck()

    def fill_deck(self):
        for value in Deck.values:
            for suit in Deck.suits:
                self.deck.append(value + suit)

d = Deck()

        