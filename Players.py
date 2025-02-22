#--------------------------------[CLI_Deck_of_Cards::M@tchu Pichu, XXI-II-'XXV]-----------------------------#
#---------------------------------------------------[Players]-----------------------------------------------#
import Table_Top
import Deck_Standard
import random
import time

class Player:
    def __init__(self, hand):
        self.hand = hand

    def print_hand(self):
        print(self.hand)

user = Player([])
house = Player([])
    #Note: #print(C10.name) # use this to print the name of the card in place of it's memory location

#--------------------------------[Dealer Functions]------------------------------------#
def deal_one_player():
    card = (random.choice(deck))
    print("You were dealt", card.name)
    #deck.pop(card.id)
    deck.remove(card)
    user.hand.append(card)

def deal_two_player():
    deal_one_player()
    deal_one_player()

def deal_bj_player_start():
    deal_two_player()

def hit():
    deal_one_player()

def show_cards_left():
    print("There are", len(deck), "cards remaining in the deck")

#--------------------------------[Main Code / Testing]----------------------------------------#
