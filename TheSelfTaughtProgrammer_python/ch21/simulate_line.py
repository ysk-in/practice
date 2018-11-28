import time
import random
from queue import Queue


def simulate_line(sell_sec, max_time_sec):
    """
    チケット販売Simulate
    :param sell_sec: チケット販売期間(単位:秒)
    :param max_time_sec: 1枚のチケットが売れるまでにかかる最大の時間(単位:秒)
    :return: 売れたチケットの情報
    """
    remain_tickets = Queue()
    sold_tickets = []
    # チケットの枚数は固定で100(なんとなく)
    for i in range(100):
        remain_tickets.enqueue("ticket#" + str(i))
    # 現在時刻 + sell_sec が経過するまでチケットを販売するループ
    t_end = time.time() + sell_sec
    while time.time() < t_end and not remain_tickets.is_empty():
        # 1枚のチケットを販売する時間(秒)を生成
        sell_sec = random.randint(0, max_time_sec)
        # 1枚のチケットが売れるまでsleep
        print_sell_progress(sell_sec)
        sold_ticket = remain_tickets.dequeue()
        print("sold ticket=" + sold_ticket)
        sold_tickets.append(sold_ticket)
    return sold_tickets


def print_sell_progress(sell_sec):
    print("selling ticket", end="")
    for s in range(sell_sec):
        print(".", end="")
        time.sleep(1)
    print("")


if __name__ == "__main__":
    sold = simulate_line(sell_sec=15, max_time_sec=5)
    print(sold)
