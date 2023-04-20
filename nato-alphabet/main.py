import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

user_input = input("Enter a word:\n").upper()
result_list = [nato_dict[letter] for letter in user_input]
print(result_list)
