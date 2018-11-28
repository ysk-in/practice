import sys
import re

# import thisのprintによるstdout出力を抑止するため stdoutを一時的に無効化する
org_sys_stdout = sys.stdout
f = open('nul', 'w')
sys.stdout = f

import this

# import this実行が終わったため stdoutを元に戻す
sys.stdout = org_sys_stdout


def get_zen():
    """
    import thisからのコピペ
    """
    return "".join([this.d.get(c, c) for c in this.s])


def re_zen(pattern):
    zen = get_zen()
    # print(zen)
    for m in re.findall(pattern, zen, re.MULTILINE):
        print(m)


def mad_libs(text):
    """
    :param text: String
    with parts the user
    should fill out surrounded
    by double underscores.
    Underscores cannot
    be inside hint e.g., no
    __hint_hint__ only
    __hint__.
    """
    print("=== MAD Libs!!! ===")
    print("The original text is below:\n--- Original Text START ---\n{}\n--- Original Text END ---".format(text))
    hints = re.findall("\(\d+\)__.*?__", text)
    if hints is not None:
        for word in hints:
            new = input("Enter a {}: ".format(word))
            text = text.replace(word, new, 1)
        print()
        # mls = mls.replace("\n", "")
        print(text)
    else:
        print("invalid mls")


def exec_mad_libs():
    text = """\
Giraffes have aroused the curiosity of (1)__PLURAL_NOUN__ since earliest times.
The giraffe is the tallest of all living (2)__PLURAL_NOUN__,\
but scientists are unable to explain how it got its long (3)__PART_OF_THE_BODY__.
The giraffe's tremendous height, which might reach (4)__NUMBER__ (5)__PLURAL_NOUN__,\
 comes from it legs and (6)__BODYPART__.\
"""
    mad_libs(text)


def exec_ch1():
    zen = get_zen()
    print(re.findall(".*Dutch.*", zen, re.MULTILINE))


def exec_ch2():
    line = "Arizona 479, 501, 870. California 209, 213, 650."
    print(re.findall("\d+", line))


def exec_ch3():
    zen = get_zen()
    line = "The ghost that says boo haunts the loo"
    base_pattern = "[A-Za-z]+oo"
    patterns = [base_pattern, ".*" + base_pattern + ".*"]
    for i, pattern in enumerate(patterns):
        print("pattern({})={} text={}"
              " findall={}".format(i, pattern, "$zen", re.findall(pattern, zen, re.MULTILINE)))
        print("pattern({})={} text={}"
              " findall={}".format(i, pattern, line, re.findall(pattern, line, re.MULTILINE)))


if __name__ == "__main__":
    # re_zen('^\s*(If.*)')
    # exec_mad_libs()
    exec_ch1()
    exec_ch2()
    exec_ch3()
