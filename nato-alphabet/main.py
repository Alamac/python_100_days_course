import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
success = False
while not success:
    user_input = input("Enter a word:\n").upper()
    try:
        result_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        success = True
        print(result_list)