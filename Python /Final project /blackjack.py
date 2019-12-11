#!/usr/bin/env python

# Make sure you read the README before starting.
# Additionally, I encourage you to read through the skeleton code 
# to get a full picture of what's going on. Try not to reinvent the 
# wheel.

import random

# Potentially Helpful Constants
SUITS = [u'\u2663', u'\u2666', u'\u2665', u'\u2660']
FACE_CARDS = ['J', 'Q', 'K']
NUMBERS = [2, 3, 4, 5, 6, 7, 8, 9, 10]


class Card(object):
    """
    Represents a standard numerical playing card.
    Posesses a suit (diamonds, clubs, hearts, or spades) and a rank 
    (2 through 10).
    For standard playing cards, the soft and hard values are equal to 
    the rank.
    """
    ###################################################################


class Card:
    def __init__(self, rank, suit):
        self.__suit = suit
        self.__rank = rank

    def __str__(self):
        return f"{self.__rank}{self.__suit}"

    def soft_value(self):
        return self.__rank

    def hard_value(self):
        return self.__rank

    def get_rank(self):
        return self.__rank

    def set_rank(self, rank):
        self.__rank = rank

    def get_suit(self):
        return self.__suit

    def set_suit(self, suit):
        self.__suit = suit

    ###################################################################


class FaceCard(Card):
    """
    Represents a Face Card (Jack, Queen, King).
    Posesses a suit.
    """

    ###################################################################

    def __init__(self, rank, suit):
        Card.__init__(self, 10, suit)

    def soft_value(self):
        return 10

    def hard_value(self):
        return 10

        ###################################################################


class AceCard(Card):
    """
    Represents an Ace Card posessing a suit.
    """

    ###################################################################

    def __init__(self, suit):
        Card.__init__(self, 'A', suit)

    def soft_value(self):
        return 11

    def hard_value(self):
        return 1

    ###################################################################


class Deck:
    """
    A Deck represents the table's deck of cards, which is used to create
    a Hand (collection of cards).
    """

    def __init__(self):
        self.__cards = self.__load_deck()

    def __shuffle(self, deck):
        random.shuffle(deck)

    def __load_deck(self):

        DeckCards = []

        for s in SUITS:
            A_card = AceCard(s)
            DeckCards.append(A_card)
            for f in FACE_CARDS:
                F_card = FaceCard(f, s)
                DeckCards.append(F_card)
            for n in NUMBERS:
                N_card = Card(n, s)
                DeckCards.append(N_card)
        self.__shuffle(DeckCards)
        return DeckCards

        """
        Creates a deck of 52 cards. Consists of 4 suits, each of which 
        contain, 2-10, J, Q, K, A.
        """
        ###################################################################

        ###################################################################

    def deal_card(self):
        """
        Removes a Card from the Deck and returns it so that it can
        enter play. If the deck is empty, deal_card() should create a 
        new deck, shuffle it, and deal a card.
        """
        ###################################################################

        return self.__cards.pop(0)

        ###################################################################


class Hand:
    """
    A Hand represents a player's current hand of cards.
    """

    def __init__(self):
        self.__cards = []
        self.__index = 1

    def __iter__(self):
        """
        Called when an iterator is requested for this object
        """
        self.__index = 1
        return self

    def __next__(self):
        """
        Called when the next() method is called on an iterator of this
        object.
        """
        try:
            card = self.__cards[self.__index]
            self.__index += 1
        except IndexError:
            raise StopIteration
        else:
            return card

    def get_hole_card(self):
        """
        Returns the hole card, but doesn't remove it from the Hand.
        """
        return self.__cards[0]

    def clear(self):
        """
        Removes all cards from the Hand in prep for another round
        """
        self.__cards = []
        self.__index = 1
        ###################################################################

        ###################################################################

    def add_card(self, card):
        """
        Adds a Card to the Hand. If the Hand is empty, the card should go
        into the hole; otherwise, the card should be showing.
        """
        ###################################################################
        self.__cards.append(card)
        self.__index += 1

        ###################################################################

    def get_soft_score(self):
        """
        Loops over the Cards in the Hand and returns the soft score
        """
        ###################################################################

        score = 0
        for c in self.__cards:
            score += c.soft_value()
        return score

        ###################################################################

    def get_hard_score(self):
        """
        Loops over the Cards in the Hand and returns the hard score
        """
        ###################################################################
        score = 0
        for c in self.__cards:
            score += c.hard_value()
        return score

        ###################################################################


class Game(object):
    """
    Represents a two player game of Blackjack. Has a deck, the player's
    hand, and the house's hand.
    """

    def __init__(self):
        self.__deck = Deck()
        self.__player = Hand()
        self.__dealer = Hand()

    def __print_player(self):
        """
        Prints the state of the Player's Hand to the Screen. Displays the 
        Hard and Soft Scores for the current state of the Hand.
        """
        print(f'Player: [Hard: {self.__player.get_hard_score()} Soft: {self.__player.get_soft_score()}]')
        print(self.__player.get_hole_card(), end=" ")
        for card in self.__player:
            print(card, end=" ")
        print()

    def __print_dealer(self):
        """
        Prints the state of the Dealer's Hand to the Screen.
        """

        print(f"Dealer:")
        for card in self.__dealer:
            print(card, end=" ")
        print()

    def __print_complete_dealer(self):
        """
        Prints the full state of the Dealer's Hand to the screen.
        """
        print(f"Dealer: [Hard: {self.__dealer.get_hard_score()} Soft: {self.__dealer.get_soft_score()}]")
        print(self.__dealer.get_hole_card(), end=" ")
        for card in self.__dealer:
            print(card, end=" ")
        print()

    def __deal_cards_to_player(self, number):
        """
        Gets the number of cards from the Deck and adds to player's hand.
        """
        for _ in range(number):
            card = self.__deck.deal_card()
            self.__player.add_card(card)

    def __deal_cards_to_dealer(self, number):
        """
        Gets the number of cards from the Deck and adds to dealer's hand.
        """
        for _ in range(number):
            card = self.__deck.deal_card()
            self.__dealer.add_card(card)

    def __check_if_player_busts(self):
        """
        Returns True if the player has busted (Hard Score is > 21), else
        returns False.
        """
        ###################################################################

        player_soft_score = self.__player.get_soft_score()
        player_hard_score = self.__player.get_hard_score()
        if player_soft_score > 21 and player_hard_score > 21:
            return True
        elif player_soft_score > 21 and player_hard_score <= 21:
            return False
        else:
            return False

        ###################################################################

    def __dealer_ai(self):
        """
        The Dealer AI. Dealer continue's to hit as long as it is below 17.
        If the house has 21, it stops immediately
        """
        soft_score = self.__dealer.get_soft_score()
        hard_score = self.__dealer.get_hard_score()

        if soft_score == 21:
            return

        while hard_score < 17:
            card = self.__deck.deal_card()
            self.__dealer.add_card(card)
            hard_score = self.__dealer.get_hard_score()

    def __check_winning_states(self):
        """
        Checks for the winning states. See README for winnings states.
        """
        ###################################################################
        player_hard_score = self.__player.get_hard_score()
        player_soft_score = self.__player.get_soft_score()
        dealer_hard_score = self.__dealer.get_hard_score()
        dealer_soft_score = self.__dealer.get_soft_score()

        if dealer_hard_score > 21:
            print("you win, dealer loses!")
        elif player_hard_score > 21:
            print("you lose, dealer wins")
        elif player_hard_score == 21 or player_soft_score == 21:
            print("you win, dealer loses!")
        elif dealer_hard_score == 21 or dealer_soft_score == 21:
            print("you lose, dealer wins")
        else:
            dealer_score = dealer_soft_score
            if dealer_soft_score > 21:
                dealer_score = dealer_hard_score

            player_score = player_soft_score
            if player_soft_score > 21:
                player_soft_score = player_hard_score

            if player_score >= dealer_score:
                print("you win, dealer loses!")
            else:
                print("you lose, dealer wins")

        ###################################################################

    def __start_new_hand(self):
        """
        Clears the Player and Dealer's Hands and deals 2 new cards to each.
        """
        self.__player.clear()
        self.__dealer.clear()
        self.__deal_cards_to_player(2)
        self.__deal_cards_to_dealer(2)

    def __prompt(self, prompt, choices):
        action = input(prompt)
        if action in choices:
            return action
        else:
            print("Invalid selection")
            return self.__prompt(prompt, choices)

    def play(self):
        """
        Plays a new hand.
        """
        self.__start_new_hand()

        while True:
            self.__print_dealer()
            self.__print_player()

            decision = self.__prompt("Would you like to [h]it, [s]tay, or [q]uit? ", ['q', 's', 'h'])

            if decision == 'h':
                self.__deal_cards_to_player(1)
                if self.__check_if_player_busts():
                    self.__print_complete_dealer()
                    self.__print_player()
                    self.__check_winning_states()
                    break

            elif decision == 's':
                self.__dealer_ai()
                self.__print_complete_dealer()
                self.__print_player()
                self.__check_winning_states()
                break

            elif decision == 'q':
                exit()

        play_again = self.__prompt("Play Again? [y]es, [n]o: ", ['y', 'n'])
        if play_again == 'y':
            self.play()
        else:
            exit()


def main():
    game = Game()
    game.play()

    print("Thanks for playing. :D")


if __name__ == "__main__":
    main()
