#!/usr/local/bin/python3
import random
#import pdb needed when debugging
#pdb.set_trace() might be needed for debugging
# war, the card game of chance where 26 battles take place between rival armies.
# the higher card wins each battle. ties accumulate a bonus to be won at the next battle.
# for each battle, outputs the number of cards left, the two cards drawn, and the win totals.
# if a battle is a tie, its value is accrued towards the next one that is won.

# build deck list, containing tuples of the names and values of each card
# the order of the names list determines the cards' values
# CORRECTION the deck is 52 tuples like this:  ('Jack of Diamonds', 9*) (CORRECTION: its value is 9 not 11)
names = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' ]
suits = [ 'Hearts', 'Diamonds', 'Spades', 'Clubs' ]
#CORRECTION :create a deck each cad has a name , a suit & a value .The value correspond at it index in names
#CORRECTION i.e. not  suits.index(suit) but names.index(name)
deck = [ (name + ' of ' + suit, names.index(name) ) for name in names for suit in suits ]
#CORRECTION:# add shuffle the deck
random.shuffle(deck)
bonus, scoreA, scoreB = 0, 0, 0

# as long as there are cards left in the deck, draw pairs for each battle
# while loop is safe as long as the only thing that happens to deck is .pop()
while deck:
 # compare a pair of cards' values, tally scores and adjust bonus
 # there are three possible cases; in case of a win the bonus is paid out, otherwise it rises
 cardA, cardB = deck.pop(), deck.pop()
 if int(cardA[1]) == int(cardB[1]): #CORRECTION integer values of cardA & cardB are compared
  bonus += 1 #CORRECTION bonus is increased by 1, not by score A
  outcome = 'ties'
 elif int(cardA[1]) > int(cardB[1]): #CORRECTION integer values of cardA & cardB are compared
  scoreA += 1 + bonus
  bonus = 0
  outcome = 'beats'
 else:
  scoreB += 1 + bonus  #CORRECTION B wins so scoreB (not scoreA) got +1 + bonus
  bonus = 0
  outcome = 'is beaten by'

 # display the outcome of each battle, current winnings, and how much left to be won
 event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0] )
 print ( '{:55.55}  ${} to ${}, ${} left.'.format ( event, scoreA, scoreB, int(len(deck)/2) ) )
#REMARK: scoreA+scoreB should be 26