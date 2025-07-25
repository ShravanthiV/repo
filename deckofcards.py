class Card:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"
    ]

    def __init__(self, number):
        self.number = number
        self.suit = number // 13       # 0 to 3
        self.rank = number % 13        # 0 to 12

    def __repr__(self):
        return f"{Card.RANKS[self.rank]} of {Card.SUITS[self.suit]}"

class Deck:
    def __init__(self):
        self.cards = [Card(i) for i in range(52)]

    def show(self, count=5):
        return self.cards[:count]

    def shuffle(self):
        import random
        random.shuffle(self.cards)

# 🃏 Usage
deck = Deck()
print("First 5 cards in order:")
print(deck.show())

deck.shuffle()
print("\nFirst 5 cards after shuffle:")
print(deck.show())
