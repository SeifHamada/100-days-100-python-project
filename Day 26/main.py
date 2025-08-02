import pandas

data = pandas.read_csv("nato.csv")

alpha_to_nato = {row.letter:row.code for (index, row) in data.iterrows()}

user = input("Enter a word: ").upper()
output = [alpha_to_nato[letter] for letter in user]
print(output)
