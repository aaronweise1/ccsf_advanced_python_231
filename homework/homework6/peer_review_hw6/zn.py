####################################################################
#  CS231  Lab 6                                                    #
#  Debug /users/abrick/resources/war-buggy.py using the            #
#  interactive debugger and send in the correctly working program  #                                                         #
#  Student Name:      James Lin  JamesLin288@gmail.com             #
#  Instructor Name:   Aaron Brick  uABrick@tccsf.edu               #
####################################################################

#!/usr/local/bin/python3
import random
import pdb

# war, the card game of chance where 26 battles take place between rival armies.
# the higher card wins each battle. ties accumulate a bonus to be won at the next battle.
# for each battle, outputs the number of cards left, the two cards drawn, and the win totals.
# if a battle is a tie, its value is accrued towards the next one that is won.

# build deck list, containing tuples of the names and values of each card
# the order of the names list determines the cards' values
# the deck is 52 tuples like this:  ('Jack of Diamonds', 11)
names = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' ]
suits = [ 'Hearts', 'Diamonds', 'Spades', 'Clubs' ]
# use name index instead of suits index
#deck = [ (name + ' of ' + suit, suits.index(suit) ) for name in names for suit in suits ]
deck = [ (name + ' of ' + suit,  names.index(name) ) for name in names for suit in suits ]
bonus, scoreA, scoreB = 0, 0, 0
# need to shuffle the deck
random.shuffle(deck) 
# as long as there are cards left in the deck, draw pairs for each battle
# while loop is safe as long as the only thing that happens to deck is .pop()
while deck:
 # compare a pair of cards' values, tally scores and adjust bonus
 # there are three possible cases; in case of a win the bonus is paid out, otherwise it rises
# i = random.randint(0,len(deck)-1)
 cardA, cardB = deck.pop(), deck.pop()
 if cardA[1] == cardB[1]:
  bonus += scoreA
  outcome = 'ties'
 elif cardA[1] > cardB[1]:
  scoreA += 1 + bonus
  bonus = 0
  outcome = 'beats'
 else:
#  scoreA += 1 + bonus
  scoreB += 1 + bonus
  bonus = 0
# move the line one space to the righ for  else  
  outcome = 'is beaten by'        
 # display the outcome of each battle, current winnings, and how much left to be won
 event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0] )
# print ( '{:55.55}  ${} to ${}, ${} left.'.format ( event, scoreA, scoreB, int(len(deck)/2) ) )
 print ( '{:55.55} Player A = ${} vs Player B = ${}, {} cards left.'.format ( event, scoreA, scoreB, int(len(deck)/2)*2 ) )

###################      Sample Output    ####################### 
#The Nine of Hearts beats the Four of Diamonds!          Player A = $1 vs Player B = $0, 50 cards left.
#The Six of Diamonds is beaten by the Eight of Clubs!    Player A = $1 vs Player B = $1, 48 cards left.
#The Ace of Spades beats the Ten of Hearts!              Player A = $2 vs Player B = $1, 46 cards left.
#The Ace of Clubs beats the Two of Diamonds!             Player A = $3 vs Player B = $1, 44 cards left.
#The Seven of Clubs is beaten by the Nine of Diamonds!   Player A = $3 vs Player B = $2, 42 cards left.
#The Five of Clubs is beaten by the Six of Clubs!        Player A = $3 vs Player B = $3, 40 cards left.
#The Seven of Diamonds beats the Three of Hearts!        Player A = $4 vs Player B = $3, 38 cards left.
#The Nine of Clubs beats the Eight of Spades!            Player A = $5 vs Player B = $3, 36 cards left.
#The Jack of Diamonds beats the Two of Hearts!           Player A = $6 vs Player B = $3, 34 cards left.
#The Jack of Spades beats the Six of Hearts!             Player A = $7 vs Player B = $3, 32 cards left.
#The Three of Diamonds is beaten by the Jack of Hearts!  Player A = $7 vs Player B = $4, 30 cards left.
#The King of Clubs beats the Queen of Spades!            Player A = $8 vs Player B = $4, 28 cards left.
#The Ten of Clubs beats the Eight of Hearts!             Player A = $9 vs Player B = $4, 26 cards left.
#The Four of Spades is beaten by the Seven of Spades!    Player A = $9 vs Player B = $5, 24 cards left.
#The Ten of Diamonds is beaten by the King of Hearts!    Player A = $9 vs Player B = $6, 22 cards left.
#The Six of Spades is beaten by the Seven of Hearts!     Player A = $9 vs Player B = $7, 20 cards left.
#The Four of Clubs is beaten by the Nine of Spades!      Player A = $9 vs Player B = $8, 18 cards left.
#The Five of Hearts is beaten by the Ten of Spades!      Player A = $9 vs Player B = $9, 16 cards left.
#The King of Diamonds beats the Four of Hearts!          Player A = $10 vs Player B = $9, 14 cards left.
#The Queen of Hearts ties the Queen of Diamonds!         Player A = $10 vs Player B = $9, 12 cards left.
#The Eight of Diamonds beats the Three of Clubs!         Player A = $21 vs Player B = $9, 10 cards left.
#The King of Spades beats the Five of Diamonds!          Player A = $22 vs Player B = $9, 8 cards left.
#The Five of Spades is beaten by the Jack of Clubs!      Player A = $22 vs Player B = $10, 6 cards left.
#The Two of Spades is beaten by the Queen of Clubs!      Player A = $22 vs Player B = $11, 4 cards left.
#The Ace of Hearts beats the Three of Spades!            Player A = $23 vs Player B = $11, 2 cards left.
#The Ace of Diamonds beats the Two of Clubs!             Player A = $24 vs Player B = $11, 0 cards left.

