import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_codes = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_codes)
is_on = True

while is_on:
    name = input("Enter Name: ").upper()
    try:
        result = [nato_codes[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        is_on = True
    else:
        print(result)
        is_on = False

