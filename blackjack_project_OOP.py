import random
import os


class UI():
    def __init__(self):
        self.playground = True
        self.deck = []
        # self.dealer= Dealer()

    def play_game(self):
        while self.playground:
            print('Welcome to BlackJack Table 1!')
            input("Please press any key to continue.")
            dealer = Dealer()
            new_deck = dealer.shuffle()
            player = Player()
            player.deal(new_deck)
            player.counting(new_deck)

            value = input("Please type quit to stop playing.")
            if value == 'quit':
                self.playground = False
                print("Thanks for playing.")
                return


class Dealer(UI):
    def __init__(self):
        super().__init__()
        self.facevalues = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
        self.suits = ['spades', 'hearts', 'diamonds', 'clubs']
        self.new_shuffle_deck = []

    def shuffle(self):
        for suit in self.suits:
            for card in self.facevalues:
                new_card = Card(card, suit)
                self.new_shuffle_deck.append(new_card)
        return self.new_shuffle_deck


class Card():
    def __init__(self, card, suit):
        self.card = card
        self.suit = suit


class Player(Dealer):
    def __init__(self):
        super().__init__()
        self.playerhand = []
        self.dealerhand = []
        self.points = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
                       8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.player_hit = True
        self.player_stand = True

    def deal(self, new_deck):
        card = random.choice(new_deck)
        self.playerhand.append(card)

        card = random.choice(new_deck)
        self.dealerhand.append(card)

        card = random.choice(new_deck)
        self.playerhand.append(card)
        print(
            f"You have been dealt {self.playerhand[0].card} of {self.playerhand[0].suit} and {self.playerhand[1].card} of {self.playerhand[1].suit}.")

        card = random.choice(new_deck)
        self.dealerhand.append(card)
        print(
            f"Dealer is showing {self.dealerhand[0].card} of {self.dealerhand[0].suit}.")

    def counting(self, new_deck):
        player_done = False
        # first_card = self.playerhand[0].card
        # self.points[first_card]
        # second_card = self.playerhand[1].card
        # self.points[second_card]
        phrase = self.player_hand_str(self.playerhand)

        total = self.calulate_score_total(self.playerhand)
        # total = self.points[first_card] + self.points[second_card]
        if total == 21:
            print(f"Congrats!! You have {phrase} and have won Blackjack!!")
            return
        else:
            print(f"You have {phrase}have {total} points")

        dealer_first_run = True
        while self.player_hit:
            phrase = self.player_hand_str(self.playerhand)

            if total == 21:
                print(f"{phrase}Congrats you hit 21!!")
                return
            if total < 21 and player_done == False:
                response = input(
                    "Would you like to hit or stand [type: hit or stand]? ")

            if response.lower() == 'hit':
                card = random.choice(new_deck)
                self.playerhand.append(card)

                for i in range(2, len(self.playerhand)):
                    # next_card = self.playerhand[i].card
                    phrase = self.player_hand_str(self.playerhand)
                    total = self.calulate_score_total(self.playerhand)
                    # print(
                    #     f"{ self.playerhand[i].card} of {self.playerhand[i].suit} and you have {total} points.")
                    print(f"You have {phrase}have {total} points")
                    if total > 21:
                        print(
                            f"You have {total} points so you have busted.")
                        return

            if response.lower() == 'stand':
                # self.player_hit = False
                if player_done == False:
                    print("Player stands")
                    print("Dealer show your cards: ")
                    player_done = True

                if dealer_first_run: 
                    dealer_first_card = self.dealerhand[0].card
                    self.points[dealer_first_card]
                    dealer_second_card = self.dealerhand[1].card
                    self.points[dealer_second_card]

                    dealer_total = self.calulate_score_total(self.dealerhand)
                    dealer_first_run = False

                for i in range(1, len(self.dealerhand)):
                    dealer_next_card = self.dealerhand[i].card
                    dealer_total = self.calulate_score_total(self.dealerhand)
                    phrase = self.player_hand_str(self.dealerhand)

                    if "A" == self.dealerhand[i].card:
                        # print("it has an 'A'.")
                        # print(f"dealer has {phrase}total of {dealer_total} points.")
                        if dealer_total >= 17 and dealer_total < 21:
                            phrase = self.player_hand_str(self.dealerhand)
                            print(
                                f"dealer has {phrase}total of {dealer_total} points.")
                            self.player_hit = False
                        elif dealer_total == 21:
                            print(
                                f"dealer will stand with {phrase}not take anymore cards and has {dealer_total} points. Dealer Wins.")
                            self.player_hit = False
                        elif dealer_total < 17:
                            if dealer_total < 22:
                                print("Dealer need to take a card")
                                dealer_card = random.choice(new_deck)
                                self.dealerhand.append(dealer_card)
                                dealer_total = self.calulate_score_total(self.dealerhand)
                                phrase = self.player_hand_str(self.dealerhand)
                                dealer_total = self.calulate_score_total(self.dealerhand)
                                print(
                                    f"dealer has {phrase}total of {dealer_total} points.")

                                # self.player_hit = False
                            else:
                                print(
                                    f"dealer will stand with {phrase}not take anymore cards and has {dealer_total} points. Dealer Busts.")
                                self.player_hit = False
                        else:
                            self.player_hit = False

                    else:
                       
                        if dealer_total >= 17 and dealer_total < 21:
                            phrase = self.player_hand_str(self.dealerhand)
                            print(
                                f"dealer has {phrase}total of {dealer_total} points.")
                            self.player_hit = False
                        elif dealer_total == 21:
                            print(
                                f"dealer will stand with {phrase}not take anymore cards and has {dealer_total} points. Dealer Wins.")
                            self.player_hit = False
                        elif dealer_total < 17:
                            if dealer_total < 22:
                                print("Dealer need to take a card")
                                dealer_card = random.choice(new_deck)
                                self.dealerhand.append(dealer_card)
                                dealer_total = self.calulate_score_total(self.dealerhand)
                                phrase = self.player_hand_str(self.dealerhand)
                                print(
                                    f"dealer has {phrase}total of {dealer_total} points.")

                            else:
                                print(
                                    f"dealer will stand with {phrase}not take anymore cards and has {dealer_total} points. Dealer Busts.")
                                self.player_hit = False
                        else:
                            self.player_hit = False
            if total < dealer_total and dealer_total  < 22 and total < 22:
                print("Dealer wins")  
            else:
                print("Player wins")              

    def player_hand_str(self, hand):
        list_of_cards = []
        for card in hand:
            list_of_cards.append(f"{card.card} of {card.suit} and ")
        return "".join(list_of_cards)

    def calulate_score_total(self,player_hand):
        score = 0
        for hand in player_hand:
            if hand.card == "K" or hand.card == "Q" or hand.card == "J" or hand.card == 10:
                score += 10
            elif hand.card == 2 or hand.card == 3 or hand.card == 4 or hand.card == 5 or hand.card == 6 or hand.card == 7 or hand.card == 8 or hand.card == 9:
                score += hand.card
            else:
                high = score + 11
                
                if high <= 21:
                    score += 11
                else:
                    score += 1
        return score
                

        

def main():

    ui = UI()
    ui.play_game()


if __name__ == "__main__":
    main()
