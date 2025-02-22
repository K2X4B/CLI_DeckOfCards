#--------------------------------[CLI_Deck_of_Cards]-----------------------------#
#---------------------------[by M@tchu Pichu, XXI-II-'XXV]----------------------#
import Table_Top
import Deck_Standard
import Players
import random
import time

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