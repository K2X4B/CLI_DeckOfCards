import random
import time

class Card:

    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def set_suit(self, suit):
        self.suit = suit

HA = Card("ace", 1, "heart")
H2 = Card("2", 2, "heart")
H3 = Card("3", 3, "heart")
H4 = Card("4", 4, "heart")
H5 = Card("5", 5, "heart")
H6 = Card("6", 6, "heart")
H7 = Card("7", 7, "heart")
H8 = Card("8", 8, "heart")
H9 = Card("9", 9, "heart")
H10 = Card("10",10 , "heart")
HJ = Card("jack", 10, "heart")
HQ = Card("queen", 10, "heart")
HK = Card("king", 10, "heart")

DA = Card("ace", 1, "diamond")
D2 = Card("2", 2, "diamond")
D3 = Card("3", 3, "diamond")
D4 = Card("4", 4, "diamond")
D5 = Card("5", 5, "diamond")
D6 = Card("6", 6, "diamond")
D7 = Card("7", 7, "diamond")
D8 = Card("8", 8, "diamond")
D9 = Card("9", 9, "diamond")
D10 = Card("10",10 , "diamond")
DJ = Card("jack", 10, "diamond")
DQ = Card("queen", 10, "diamond")
DK = Card("king", 10, "diamond")

SA = Card("ace", 1, "spade")
S2 = Card("2", 2, "spade")
S3 = Card("3", 3, "spade")
S4 = Card("4", 4, "spade")
S5 = Card("5", 5, "spade")
S6 = Card("6", 6, "spade")
S7 = Card("7", 7, "spade")
S8 = Card("8", 8, "spade")
S9 = Card("9", 9, "spade")
S10 = Card("10",10 , "spade")
SJ = Card("jack", 10, "spade")
SQ = Card("queen", 10, "spade")
SK = Card("king", 10, "spade")

CA = Card("ace", 1, "club")
C2 = Card("2", 2, "club")
C3 = Card("3", 3, "club")
C4 = Card("4", 4, "club")
C5 = Card("5", 5, "club")
C6 = Card("6", 6, "club")
C7 = Card("7", 7, "club")
C8 = Card("8", 8, "club")
C9 = Card("9", 9, "club")
C10 = Card("10",10 , "club")
CJ = Card("jack", 10, "club")
CQ = Card("queen", 10, "club")
CK = Card("king", 10, "club")