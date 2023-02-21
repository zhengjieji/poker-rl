"""
Define the objects used in the Texas Hold'em game.
"""

import random

class Card(object):
    """
    A card has a suit and a rank.
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit

    def __cmp__(self, other):
        """
        Compare two cards.
        """
        # check the ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # ranks are the same... check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # ranks and suits are the same... it's a tie
        return 0

class Deck(object):
    """
    A deck of cards.
    """
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """
        Build a deck of 52 cards.
        """
        for s in ['C', 'D', 'H', 'S']:
            for r in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(s, r))

    def show(self):
        """
        Show all the cards in the deck.
        """
        for c in self.cards:
            print c

    def shuffle(self):
        """
        Shuffle the deck.
        """
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        """
        Draw a card from the deck.
        """
        return self.cards.pop()

class Player(object):
    """
    A player in the game.
    """
    def __init__(self, name, money):
        self.name = name
        self.hand = []
        self.money = money

    def draw(self, deck):
        """
        Draw a card from the deck and add it to the player's hand.
        """
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        """
        Show the player's hand.
        """
        for card in self.hand:
            print card

    def discard(self):
        """
        Discard the player's hand.
        """
        self.hand = []
        return self

    def showMoney(self):
        """
        Show the player's money.
        """
        print self.money
        return self

    def addMoney(self, amount):
        """
        Add money to the player's money.
        """
        self.money += amount
        return self

    def subtractMoney(self, amount):
        """
        Subtract money from the player's money.
        """
        self.money -= amount
        return self

class Dealer(object):
    """
    The dealer in the game.
    """
    def __init__(self, name):
        self.name = name

    def deal(self, deck, players):
        """
        Deal two cards to each player.
        """
        for i in range(2):
            for player in players:
                player.draw(deck)
        return self

    def showAllHands(self, players):
        """
        Show all the players' hands.
        """
        for player in players:
            player.showHand()
        return self

    def discardAllHands(self, players):
        """
        Discard all the players' hands.
        """
        for player in players:
            player.discard()
        return self

    def burnCard(self, deck):
        """
        Burn a card from the deck.
        """
        deck.drawCard()
        return self

class Pot(object):
    """
    The pot in the game.
    """
    def __init__(self):
        self.amount = 0

    def add(self, amount):
        """
        Add money to the pot.
        """
        self.amount += amount
        return self

    def show(self):
        """
        Show the amount of money in the pot.
        """
        print self.amount
        return self

    def reset(self):
        """
        Reset the pot.
        """
        self.amount = 0
        return self

class Table(object):
    """
    The table in the game.
    """
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        """
        Add a card to the table.
        """
        self.cards.append(card)
        return self

    def showCards(self):
        """
        Show the cards on the table.
        """
        for card in self.cards:
            print card
        return self

    def reset(self):
        """
        Reset the table.
        """
        self.cards = []
        return self
