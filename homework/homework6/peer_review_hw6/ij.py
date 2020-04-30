# the code was debugged from command prompt using the pdb command line tools
import random


names = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' ]
suits = [ 'Hearts', 'Diamonds', 'Spades', 'Clubs' ]
deck = [ (name + ' of ' + suit, suits.index(suit) ) for name in names for suit in suits ]
bonus, scoreA, scoreB = 0, 0, 0
while deck:
   cardA, cardB = deck.pop(), deck.pop()
   if cardA[1] == cardB[1]: #checking the card
       bonus += scoreA
       outcome = 'ties'
       event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0] )
       print ( '{:55.55} ${} to ${}, ${} left.'.format ( event, scoreA, scoreB, int(len(deck)/2) ) )
   elif cardA[1] > cardB[1]:
       scoreA += 1 + bonus
       bonus = 0
       outcome = 'beats'
       event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0] )
       print ( '{:55.55} ${} to ${}, ${} left.'.format ( event, scoreA, scoreB, int(len(deck)/2) ) )
   else:
       scoreA += 1 + bonus
       bonus = 0
       outcome = 'is beaten by'
       event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0] )
       print ( '{:55.55} ${} to ${}, ${} left.'.format ( event, scoreA, scoreB, int(len(deck)/2) ) )
