from enum import Enum, auto


class Suit(Enum):
    # 定数値はスートの強さ SPADESが一番弱くて CLUBSが一番強い
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUB = 3


class Card:
    # indexと値を揃えるため要素0はNone 1は強いカード(Ace)として扱うためNone
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]
    # valuesの要素が始まるIndex(先頭None無視するため) forループ回す用途
    values_start_index = 2

    # Card種類 検算用途
    CARD_NUM = 52

    def __init__(self, v, s):
        """
        vは2から14の数字が指定可能
        sはSuitが指定可能
        """
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suit.value < c2.suit.value:
                return True
        return False

    def __gt__(self, c2):
        return c2.__lt__(self)

    def __repr__(self):
        # v = str.format("{:>5}", Card.values[self.value]) + " of " + self.suit.name
        v = str.format("{}", Card.values[self.value]) + " of " + self.suit.name
        return v


def tests():
    card1 = Card(2, Suit.SPADE)
    print(card1)


if __name__ == "__main__":
    tests()
