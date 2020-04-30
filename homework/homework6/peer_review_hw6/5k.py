#!/usr/local/bin/python3
# Course   : CS 231 
# Homework : 6
# Due date  :  March 15, 2020
# Filename: hw6.py

"""
Debug /users/abrick/resources/war-buggy.py using the interactive debugger and send in the correctly working program
"""

import random

# war, the card game of chance where 26 battles take place between rival armies.
# the higher card wins each battle. ties accumulate a bonus to be won at the next battle.
# for each battle, outputs the number of cards left, the two cards drawn, and the win totals.
# if a battle is a tie, its value is accrued towards the next one that is won.

# build deck list, containing tuples of the names and values of each card
# the order of the names list determines the cards' values
# the deck is 52 tuples like this:  ('Jack of Diamonds', 11)
# ('Jack of Diamonds', 11) is wrong, 'Jack;' is index 9 in names list, NOT 11
# CHANGED: example of the deck: ('Jack of Diamonds', 1, 'Jack', 9)
names = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' ]
suits = [ 'Hearts', 'Diamonds', 'Spades', 'Clubs' ]
deck = [ (name + ' of ' + suit, suits.index(suit), name, names.index(name) ) for name in names for suit in suits ] # CHANGED LINE: added "name, names.index(name)"  
bonus, scoreA, scoreB, battleNum = 0, 0, 0, 0 # CHANGED LINE: added variable 'battleNum', keep track we're on battle number what

random.shuffle(deck) # CHANGED LINE: this line added
# before: pop() remove from deck with cards already in order
# now: the deck cards are mixed for the game

# as long as there are cards left in the deck, draw pairs for each battle
# while loop is safe as long as the only thing that happens to deck is .pop()
while deck:

 # compare a pair of cards' values, tally scores and adjust bonus
 # there are three possible cases; in case of a win the bonus is paid out, otherwise it rises
 cardA, cardB = deck.pop(), deck.pop()
 if cardA[3] == cardB[3]: # CHANGED LINE: from [1] to [3], the battle is suppose to compares cards' values by its names, NOT its suit.
  bonus += 1  # CHANGED LINE: from 'scoreA' to '1', accumulate a bonus to be won at the next battle
  outcome = 'ties'
 elif cardA[3] > cardB[3]: # CHANGED LINE: from [1] to [3], the battle is suppose to compares cards' values by its names, NOT its suit.
  scoreA += 1 + bonus
  bonus = 0
  outcome = 'beats'
 else: # aka cardA[3] < cardB[3], player B won!
  scoreB += 1 + bonus # CHANGED LINE: In this case, add point for scoreB NOT scoreA
  bonus = 0
  outcome = 'is beaten by' # CHANGED LINE: Corrected indent. Before: Wrong indenting! basically all three cases' outcome end up being 'is beaten by' 
 battleNum += 1 # CHANGED LINE: line added, a counter to count we're on battle number what

 # display the outcome of each battle, current winnings, and how much left to be won
 event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0] )
 print ( '{:<2d} {:55.55}  ${} to ${}, ${} left.'.format (battleNum, event, scoreA, scoreB, int(len(deck)/2) ) ) # CHANGED LINE: added 'battleNum' to the sentence to keep track of on battle number

