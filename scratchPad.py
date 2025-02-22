#--------------------------------[CLI_Deck_of_Cards]-----------------------------#
#---------------------------[by M@tchu Pichu, XXI-II-'XXV]----------------------#
import random
import time
#--------------------------------[Card Objects]----------------------------------#
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
#----------------------------------[Hearts]---------------------------------------#
HA = Card("The ace of hearts", 1, "hearts", 1)
H2 = Card("The 2 of hearts", 2, "hearts", 2)
H3 = Card("The 3 of hearts", 3, "hearts", 3)
H4 = Card("The 4 of hearts", 4, "hearts", 4)
H5 = Card("The 5 of hearts", 5, "hearts", 5)
H6 = Card("The 6 of hearts", 6, "hearts", 6)
H7 = Card("The 7 of hearts", 7, "hearts", 7)
H8 = Card("The 8 of hearts", 8, "hearts", 8)
H9 = Card("The 9 of hearts", 9, "hearts", 9)
H10 = Card("The 10 of hearts",10 , "hearts", 10)
HJ = Card("The jack of hearts", 10, "hearts", 11)
HQ = Card("The queen of hearts", 10, "hearts", 12)
HK = Card("The king of hearts", 10, "hearts", 13)
#----------------------------------[Diamonds]---------------------------------------#
DA = Card("The ace of diamonds", 1, "diamonds", 14)
D2 = Card("The 2 of diamonds", 2, "diamonds", 15)
D3 = Card("The 3 of diamonds", 3, "diamonds", 16)
D4 = Card("The 4 of diamonds", 4, "diamonds", 17)
D5 = Card("The 5 of diamonds", 5, "diamonds", 18)
D6 = Card("The 6 of diamonds", 6, "diamonds", 19)
D7 = Card("The 7 of diamonds", 7, "diamonds", 20)
D8 = Card("The 8 of diamonds", 8, "diamonds", 21)
D9 = Card("The 9 of diamonds", 9, "diamonds", 22)
D10 = Card("The 10 of diamonds",10 , "diamonds", 23)
DJ = Card("The jack of diamonds", 10, "diamonds", 24)
DQ = Card("The queen of diamonds", 10, "diamonds", 25)
DK = Card("The king of diamonds", 10, "diamonds", 26)
#----------------------------------[Spades]---------------------------------------#
SA = Card("The ace of spades", 1, "spades", 27)
S2 = Card("The 2 of spades", 2, "spades", 28)
S3 = Card("The 3 of spades", 3, "spades", 29)
S4 = Card("The 4 of spades", 4, "spades", 30)
S5 = Card("The 5 of spades", 5, "spades", 31)
S6 = Card("The 6 of spades", 6, "spades", 32)
S7 = Card("The 7 of spades", 7, "spades", 33)
S8 = Card("The 8 of spades", 8, "spades", 34)
S9 = Card("The 9 of spades", 9, "spades", 35)
S10 = Card("The 10 of spades",10 , "spades", 36)
SJ = Card("The jack of spades", 10, "spades", 37)
SQ = Card("The queen of spades", 10, "spades", 38)
SK = Card("The king of spades", 10, "spades", 39)
#----------------------------------[Clubs]---------------------------------------#
CA = Card("The ace of clubs", 1, "clubs", 40)
C2 = Card("The 2 of clubs", 2, "clubs", 41)
C3 = Card("The 3 of clubs", 3, "clubs", 42)
C4 = Card("The 4 of clubs", 4, "clubs", 43)
C5 = Card("The 5 of clubs", 5, "clubs", 44)
C6 = Card("The 6 of clubs", 6, "clubs", 45)
C7 = Card("The 7 of clubs", 7, "clubs", 46)
C8 = Card("The 8 of clubs", 8, "clubs", 47)
C9 = Card("The 9 of clubs", 9, "clubs", 48)
C10 = Card("The 10 of clubs",10 , "clubs", 49)
CJ = Card("The jack of clubs", 10, "clubs", 50)
CQ = Card("The queen of clubs", 10, "clubs", 51)
CK = Card("The king of clubs", 10, "clubs", 52)
#--------------------------------[Player Objects]--------------------------------------#
class Player:
    def __init__(self, hand):
        self.hand = hand

    def print_hand(self):
        print(self.hand)

#--------------------------------[Player Functions]--------------------------------------#

# def show_hand():
# def discard_hand():


#--------------------------------[Table_Top]------------------------------------#
deck = [HA, H2, H3, H4, H5, H6, H7, H8, H9, H10, HJ, HQ, HK, DA, D2, D3, D4, D5, D6, D7, D8, D9, D10, DJ, DQ, DK, SA, S2, S3, S4, S5, S6, S7, S8, S9, S10, SJ, SQ, SK, CA, C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK, ]
discard_pile = []

#--------------------------------[Dealer Functions]------------------------------------#
# Generic
def deal_one_player():
    card = (random.choice(deck))
    print("You were dealt", card.name)
    #deck.pop(card.id)
    deck.remove(card)
    user.hand.append(card)

def deal_two_player():
    deal_one_player()
    deal_one_player()

# Info
def show_cards_left():
    print("There are", len(deck), "cards remaining in the deck")

# Blackjack
def deal_bj_player_start():
    deal_two_player()
## Hit
def hit():
    deal_one_player()

# Poker:
# --- Texas Hold'em:
#def  flop():
#def turn():
#def  river():

#--------------------------------[Main Code / Testing]----------------------------------------#

user = Player([])
house = Player([])
    #Note: #print(C10.name) # use this to print the name of the card in place of it's memory location


print(len(deck), " cards remaining in the deck")
deal_two_player()
#print(user.hand[0].name)
print(len(deck), " cards remaining in the deck")
#deal_one_player()
deal_bj_player_start()
print(len(deck), " cards remaining in the deck")
print("hit")
hit()
#print(len(deck), " cards remaining in the deck")
show_cards_left()