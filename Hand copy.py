def sorting(card):
    return card.value


class Hand:
    def __init__(self):
        self.hand = []

    def get_hand(self):
        return self.hand

    def add_card(self, card):
        self.hand.append(card)
        self.hand.sort(key=sorting)

    def rank(self):
        if self.is_royal_flush():
            return 9
        elif self.is_straight_flush():
            return 8
        elif self.is_four_of_a_kind():
            return 7
        elif self.is_full_house():
            return 6
        elif self.is_flush():
            return 5
        elif self.is_straight():
            return 4
        elif self.is_three_of_a_kind():
            return 3
        elif self.is_two_pair():
            return 2
        elif self.is_one_pair():
            return 1
        else:
            return 0

    def get_hand_type(self):

        if self.is_royal_flush():

            return "Royal Flush"



        elif self.is_straight_flush():

            return "Straight Flush"



        elif self.is_four_of_a_kind():

            return "Four-of-a-kind"



        elif self.is_full_house():

            return "Full House"



        elif self.is_flush():

            return "Flush"



        elif self.is_straight():

            return "Straight"



        elif self.is_three_of_a_kind():

            return "Three of a kind"



        elif self.is_two_pair():

            return "Two Pair"



        elif self.is_one_pair():

            return "One Pair"



        elif self.is_high():

            return "High card"

    def is_royal_flush(self):
        # determines whats essecaru for a hand to be considered a royal flush

        sum = 0
        for x in self.hand:
            sum += x.value()
        if sum == 60:
            for x in range(0, len(self.hand) - 1):
                if self.hand[x].suit == self.hand[x + 1].suit:
                    return False
            return True
        else:
            return False

    def is_straight_flush(self):
        # determines whats essecaru for a hand to be considered a straight flush

        for i in range(1, len(self.hand)):
            if self.hand[i].suit != self.hand[0].suit:
                return False
            for x in range(0, len(self.hand) - 1):
                if self.hand[x].suit != self.hand[x + 1].suit:
                    return False
                return True

    def is_four_of_a_kind(self):
        # determines whats essecaru for a hand to be considered a four of a kind

        for x in range(0, len(self.hand) - 1):
            if self.hand[0].value == self.hand[1].value == self.hand[2].value == self.hand[3].value:
                return True
            elif self.hand[1].value == self.hand[2].value == self.hand[3].value == self.hand[5].value:
                return True


        return False

    def is_full_house(self):
        # determines whats essecaru for a hand to be considered a full house

        if self.hand[0].value == self.hand[1].value and self.hand[1].value == self.hand[2].value:
            if self.hand[0].value == self.hand[1].value:
                return True

        elif self.hand[2].value == self.hand[3].value and self.hand[3].value == self.hand[4].value:
            if self.hand[0].value == self.hand[1].value:
                return True

    def is_flush(self):
        # determines whats essecaru for a hand to be considered a tflush

        for i in range(0, len(self.hand)):
            if self.hand[i].suit != self.hand[0].suit:
                return False
        return True


    def is_straight(self):
        # determines whats essecaru for a hand to be considered a straight

        for x in range(0, len(self.hand) - 1):
            if self.hand[x].suit == self.hand[x + 1].suit:
                return False
            return True
        else:
            return False


    def is_three_of_a_kind(self):
        # determines whats essecaru for a hand to be considered a three of a kind
        if self.hand[0].value == self.hand[1].value and self.hand[1].value == self.hand[2].value:
            return True
        if self.hand[1].value == self.hand[2].value and self.hand[2].value == self.hand[3].value:
            return True
        if self.hand[2].value == self.hand[3].value:
            return True
        else:
            return False



    def compare_two_pair(self, other_hand):
        #compares two pair and sees which player has a better hand
        if self.hand[1]>other_hand.hand[1]:
            return 1
        if self.hand[2]<other_hand.hand[2]:
            return -1
        if self.hand[1] == other_hand.hand[1]:
            if self.hand[4] > other_hand.hand[4]:
                return 1
            if self.hand[4] < other_hand.hand[4]:
                return -1
            else:
                return 0



    def compare_one_pair(self, other_hand):
        #compares one pait and sees which player has a better hand
        if self.get_value_repeat(2)[0]>other_hand.get_value(2)[0]:
            return 1
        else:
            return -1

    def compare_three_of_a_kind(self, other_hand):
        # compares three of a kind to see which hand has better cards
        if self.get_value_repeat(3)[0]>other_hand.get_value_repeat(3)[0]:
            return 1
        else:
            return -1

    def compare_full_house(self, other_hand):
        # compares full house to see which hand has better cards

        if self.get_value_repeat(3)[0]>other_hand.get_value_repeat(3)[0] and self.get_value_repeat(2)[0]>other_hand.get_value_repeat(2)[0]:
            return 1
        else:
            return -1

    def get_value_repeat(self, n):
        #if theres more than one with the same value in the player hand its a repear
        hand_value =[card.get_value() for card in self.hand]
        return [x for x in hand_value if hand_value.count(x) == n]

    def is_two_pair(self):
        # compares two pairs to see which hand has better cards

        if not self.is_three_of_a_kind() == False and not self.is_full_house() and not self.is_four_of_a_kind():
            if (self.hand[0].value == self.hand[1].value and self.hand[2].value == self.hand[3].value or self.hand[
                0].value == self.hand[1].value and self.hand[3].value == self.hand[4].value or self.hand[1].value ==
                    self.hand[2].value and self.hand[3].value == self.hand[4].value):
                return True
            return False

    def is_one_pair(self):
        #defines what a one pair is
        if self.hand[0].value == self.hand[1].value:
            return True
        if self.hand[1].value == self.hand[2].value:
            return True
        if self.hand[2].value == self.hand[3].value:
            return True
        if self.hand[3].value == self.hand[4].value:
            return True
        if self.hand[4].value == self.hand[5].value:
            return True
        else:
            return False

    def is_high(self):
        #defines what a hihgh card is
        if self.is_royal_flush() == False and self.is_straight_flush() == False and self.is_four_of_a_kind() == False and self.is_full_house() == False and self.is_flush() == False and self.is_straight() == False and self.is_three_of_a_kind() == False and self.is_two_pair() == False and self.is_one_pair():
            return True
        else:
            return False

    def is_pair(self):
        #compares pairs and sees which player has the better hand
        is_pair = False
        count = 0
        for i in range(len(self.hand) - 1):
            if self.get_card_value(i) == self.get_card_value(i + 1):
                count += 1
        if count == 1:
            is_pair = True
        return is_pair

    def comp_high(self, otherHand):
        #compares high card and sees which player has a better hand

        for x in range(0, 4):

            if self.hand[x] > otherHand.hand[x]:

                return 1

            elif self.hand[x] < otherHand.hand[x]:

                return -1

        return 0

    def repeat(self, n):
# repeats
        hand_value = [card.get_value() for card in self.hand]

        return [x for x in hand_value if hand_value.count(x) == n]


    def compare(self, otherHand):
        #comparing other hand to your own cards
        if self.rank() > otherHand.rank():
            return 1
        if self.rank() < otherHand.rank():
            return -1
        if self.rank() == 9 and otherHand.rank() == 9:
            return 0
        if self.rank() == 8 and otherHand.rank() == 8:
            return self.comp_high(otherHand)

        if self.rank() == 7 and otherHand.rank() == 7:
            return self.compare_four_of_a_kind(otherHand)

        if self.rank() == 6 and otherHand.rank() == 6:
            return self.compare_full_house(otherHand)
        if self.rank() == 5 and otherHand.rank() == 5:
            return self.comp_high(otherHand)


        if self.rank() == 4 and otherHand.rank() == 4:
            return self.comp_high(otherHand)

        if self.rank() == 3 and otherHand.rank() == 3:
            return self.compare_three_of_a_kind(otherHand)

        if self.rank() == 2 and otherHand.rank() == 2:
            return self.compare_two_pair(otherHand)

        if self.rank() == 1 and otherHand.rank() == 1:
            return self.compare_two_pair(otherHand)
        if self.rank() == 0 and otherHand.rank() == 0:
            return self.compare_one_pair(otherHand)
        else:
            return self.comp_high(otherHand)

    def print_hand(self):
        #print hands used in main class
        for p in self.hand:
            print(p.get_name())




