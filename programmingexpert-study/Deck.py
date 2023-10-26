from random import shuffle
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

    def shuffle(self):
        shuffle(self.deck)

    def deal(self, n):
        cards_dealt = []
        number_of_cards_to_deal = n
        number_of_cards_dealt = 0

        while number_of_cards_dealt < number_of_cards_to_deal:
            if len(self.deck) == 0:
                return cards_dealt
            
            cards_dealt.append(self.deck.pop())
            number_of_cards_dealt += 1

        return cards_dealt
    
    def sort_by_suit(self):
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.deck:
            suit = card[-1]
            cards_by_suit[suit].append(card)

        self.deck = (
            cards_by_suit["H"] +
            cards_by_suit["D"] +
            cards_by_suit["C"] +
            cards_by_suit["S"]
        )

    def contains(self, card):
        if card in self.deck:
            return True
        return False

    def copy(self):
        new_deck = Deck()
        new_deck.deck = self.get_cards()
        return new_deck
    
    def get_cards(self):
        return self.deck[:]
    
    def __len__(self):
        return len(self.deck)


        



d = Deck()
print('\n')
print(d.deck)
print('\n')
d.sort_by_suit()
print(d.deck)
print('\n')
d.shuffle()
print(d.deal(40))
print(len(d.deck))
d.shuffle()
print(d.deck)
#print(d.deal(45))
print(len(d.deck))
d.shuffle()
print(d.deck)
d.shuffle()
print(d.deck)
d.sort_by_suit()
print(d.deck)



        