import random

STAGE_MAX = 7


def get_word():
    # "$"は使用不可 hangman関数で見つかった文字を"$"で置換する仕様のため
    word_list = [
        "cat",
        "dog",
        "python",
        "perl",
        "clang",
        "golang",
        "java",
        "scala",
        "kotlin",
        "ruby"
    ]
    return word_list[random.randint(0, len(word_list) - 1)]


def get_stage(num):
    err_msg = "get_stageの引数numには{}以下の数値を指定してください." \
              " num={}が指定されたものとして処理を継続します.".format(STAGE_MAX, STAGE_MAX)
    try:
        num = int(num)
        if num > STAGE_MAX:
            print(err_msg)
            num = STAGE_MAX
    except BaseException as e:
        print(err_msg + " e=" + str(e))
        num = STAGE_MAX
    # STAGEの完成形は以下 STAGEが進むごとに一筆ずつ書き足す
    # line1 = ["__________  "]
    # line2 = ["|        |  "]
    # line3 = ["|        0  "]
    # line4 = ["|       /|\ "]
    # line5 = ["|       / \ "]
    # line6 = ["|           "]
    line1 = list("__________  ")
    line2 = list("|           ")
    line3 = list("|           ")
    line4 = list("|           ")
    line5 = list("|           ")
    line6 = list("|           ")
    for i in range(num):
        if num >= 1:
            line2[9] = "|"
        if num >= 2:
            line3[9] = "0"
        if num >= 3:
            line4[9] = "|"
        if num >= 4:
            line4[8] = "/"
        if num >= 5:
            line4[10] = "\\"
        if num >= 6:
            line5[8] = "/"
        if num >= STAGE_MAX:
            line5[10] = "\\"
    stage = [
        "".join(line1),
        "".join(line2),
        "".join(line3),
        "".join(line4),
        "".join(line5),
        "".join(line6)
    ]
    return "\n".join(stage)


def exec_hangman(word):
    remain_letters = list(word)
    guess_board = ["_"] * len(word)
    print("Welcome to Hangman")
    is_wrong = False
    wrong = 0
    while wrong < STAGE_MAX:
        input_letter = input("Guess a letter: ")
        if input_letter in remain_letters:
            is_wrong = False
            # inputされた文字(input_letter)が 残り文字列(remain_letters)に含まれる
            found_indexes = [i for i, letter in enumerate(remain_letters) if letter == input_letter]
            # 見つかった文字は$で置換して 重複して見つからないようにする
            for found_index in found_indexes:
                remain_letters[found_index] = '$'
                guess_board[found_index] = input_letter
            # すべての文字が見つかったら"勝ち"でゲーム終了
            if "_" not in guess_board:
                print("You win!")
                print("Guess word: " + "".join(guess_board))
                return
        else:
            is_wrong = True
            wrong += 1
        print("Remain letters: " + "".join(guess_board))
        if is_wrong:
            print("HANGMAN\n" + get_stage(wrong))
    # hangmanが完成してしまったので"負け"でゲーム終了
    print("You lose! It was {}.".format(word))
    return


if __name__ == "__main__":
    exec_hangman(get_word())
