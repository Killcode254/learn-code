# function to replace characters in  string


def replace_in(phrase):
    word = " "
    for letter in phrase:
        if letter.lower()in "aeiou":
            word = word + "g"
        else:
            word = word + letter
        return word
print(replace_in(input("enter your name")))