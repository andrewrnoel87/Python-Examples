class Deck:
    values = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    suits = ["D", "H", "C", "S"]  # Diamond, Heart, Club, Spade

    def __init__(self):
        deck = []
        