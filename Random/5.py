import random


def main(str):  # перестановка букв
    new_word = []
    new_str = ""
    for word in str.split():
        pref = word[0]
        suf = word[-1]
        middle = word[1:-1]
        middle = "".join(random.sample(middle, k=len(middle)))
        if len(word) == 1:
            new_word = word + " "
        else:
            new_word = pref + middle + suf+" "
        new_str = new_str + new_word
    return(new_str)


str = "П результатам исследования"
print(main(str))
