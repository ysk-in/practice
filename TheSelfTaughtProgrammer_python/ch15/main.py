from random import shuffle
from card import Card, Suit


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(Card.values_start_index, len(Card.values)):
            for suit in Suit:
                self.cards.append(Card(i, suit))
        # デバッグログ Cardが全種類生成できているか確認する
        # if len(self.cards) != Card.CARD_NUM:
        #     print("card num is invalid. expect={}, actual={}.".format(Card.CARD_NUM, len(self.cards)))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("プレーヤー1の名前: ")
        name2 = input("プレーヤー2の名前: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.round_count = 1

    def win_player(self, win_player):
        print("ラウンド{} は {} が勝ちました!!!".format(self.round_count, win_player.name))
        win_player.wins += 1
        self.round_count += 1

    def print_draw_info(self, p1card, p2card):
        print("{} は * {} * , {} は * {} * を引きました!".format(self.p1.name, p1card, self.p2.name, p2card))

    def print_win_player(self):
        msg = "*** {} *** の勝利です!"
        if self.p1.wins > self.p2.wins:
            print(msg.format(self.p1.name))
        elif self.p1.wins < self.p2.wins:
            print(msg.format(self.p2.name))
        else:
            print(msg="ゲーム終了, 引き分けです!")

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます!")
        while len(cards) >= 2:
            # response = input("q で終了, それ以外のキーでPlay: ")
            # if response == 'q':
            #     break
            print("--- ラウンド{}!!! ---".format(self.round_count))
            p1card = self.deck.rm_card()
            p2card = self.deck.rm_card()
            self.print_draw_info(p1card, p2card)
            if p1card > p2card:
                self.win_player(self.p1)
            else:
                # 同じ強さのカードは存在しないため引き分けは無い
                self.win_player(self.p2)
        print("=== ゲーム終了!!! ===")
        self.print_win_player()


def test_card_class():
    card1 = Card(10, Suit.DIAMOND)
    card2 = Card(11, Suit.CLUB)
    print(card1 < card2)
    print("card1={}, card2={}".format(card1, card2))
    print(len(Card.values))


def test_deck_class():
    deck = Deck()
    for i, card in enumerate(deck.cards):
        print('i={:0=2}, card={}'.format(i, card))


if __name__ == "__main__":
    # test_card_class()
    # test_deck_class()
    Game().play_game()
