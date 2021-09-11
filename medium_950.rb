require "byebug"

# 950. Reveal Cards In Increasing Order

# You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].

# You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

# You will do the following steps repeatedly until all cards are revealed:

# Take the top card of the deck, reveal it, and take it out of the deck.
# If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
# If there are still unrevealed cards, go back to step 1. Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.

# even indices are increasing order, half of the deck or deck.length/2+1
# [1,x,2,x,3,x,4,x,5]

# odd indices

# reverse the order put 1,2,3,4,5 into the deck
# 5 -> [5]
# 4 -> [4,5] -> [5,4]
# 3 -> [3, 5, 4] -> [4, 3, 5]
# 2 -> [2,4,3,5] -> [5,2,4,3]
# 1 -> [1,5,2,4,3]

def deck_revealed_increasing(deck)
  cards = deck.sort{|a,b| b<=>a}
  order = []
  # debugger
  cards.each_with_index do |card, i|
    order.unshift(card)
    order.unshift(order.pop) if i != cards.length-1
  end
  order
end


deck1 = [17,13,11,2,3,5,7]
p deck_revealed_increasing(deck1)

deck2 = [1,1000]
p deck_revealed_increasing(deck2)
