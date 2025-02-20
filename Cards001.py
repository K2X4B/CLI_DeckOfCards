import random
import time

class Card:

    def __init__(self, name, value, suit, id):
        self.name = name
        self.value = value
        self.suit = suit
        self.id = id

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit
    
    def get_id(self):
        return self.id

    def set_value(self, value): # for aces and face cards
        self.value = value

    def show(self, name, suit):
        print(f"The {name} of {suit}")


    #def set_in_deck(self):
        #self.set_in_deck = True

HA = Card("ace", 1, "heart", 1)
H2 = Card("2", 2, "heart", 2)
H3 = Card("3", 3, "heart", 3)
H4 = Card("4", 4, "heart", 4)
H5 = Card("5", 5, "heart", 5)
H6 = Card("6", 6, "heart", 6)
H7 = Card("7", 7, "heart", 7)
H8 = Card("8", 8, "heart", 8)
H9 = Card("9", 9, "heart", 9)
H10 = Card("10",10 , "heart", 10)
HJ = Card("jack", 10, "heart", 11)
HQ = Card("queen", 10, "heart", 12)
HK = Card("king", 10, "heart", 13)

DA = Card("ace", 1, "diamond", 14)
D2 = Card("2", 2, "diamond", 15)
D3 = Card("3", 3, "diamond", 16)
D4 = Card("4", 4, "diamond", 17)
D5 = Card("5", 5, "diamond", 18)
D6 = Card("6", 6, "diamond", 19)
D7 = Card("7", 7, "diamond", 20)
D8 = Card("8", 8, "diamond", 21)
D9 = Card("9", 9, "diamond", 22)
D10 = Card("10",10 , "diamond", 23)
DJ = Card("jack", 10, "diamond", 24)
DQ = Card("queen", 10, "diamond", 25)
DK = Card("king", 10, "diamond", 26)

SA = Card("ace", 1, "spade", 27)
S2 = Card("2", 2, "spade", 28)
S3 = Card("3", 3, "spade", 29)
S4 = Card("4", 4, "spade", 30)
S5 = Card("5", 5, "spade", 31)
S6 = Card("6", 6, "spade", 32)
S7 = Card("7", 7, "spade", 33)
S8 = Card("8", 8, "spade", 34)
S9 = Card("9", 9, "spade", 35)
S10 = Card("10",10 , "spade", 36)
SJ = Card("jack", 10, "spade", 37)
SQ = Card("queen", 10, "spade", 38)
SK = Card("king", 10, "spade", 39)

CA = Card("ace", 1, "club", 40)
C2 = Card("2", 2, "club", 41)
C3 = Card("3", 3, "club", 42)
C4 = Card("4", 4, "club", 43)
C5 = Card("5", 5, "club", 44)
C6 = Card("6", 6, "club", 45)
C7 = Card("7", 7, "club", 46)
C8 = Card("8", 8, "club", 47)
C9 = Card("9", 9, "club", 48)
C10 = Card("10",10 , "club", 49)
CJ = Card("jack", 10, "club", 50)
CQ = Card("queen", 10, "club", 51)
CK = Card("king", 10, "club", 52)

deck = [HA, H2, H3, H4, H5, H6, H7, H8, H9, H10, HJ, HQ, HK, DA, D2, D3, D4, D5, D6, D7, D8, D9, D10, DJ, DQ, DK, SA, S2, S3, S4, S5, S6, S7, S8, S9, S10, SJ, SQ, SK, CA, C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK, ]

class Player:
    def __init__(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand
    
    def show_hand(self):
        print(f"user's hand is {self.hand} ")
    
    def set_score(self, score):
        self.score = sum(Player.get_hand)

user = Player([])

def draw_card(self):
    C = (random.choice(deck))
    Card.show(C)
    self.hand.append(C)

draw_card(user)
print(user.show_hand())
print(user.hand)
