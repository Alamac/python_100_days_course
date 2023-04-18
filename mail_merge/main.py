letter_text = ""
with open("./Input/Letters/starting_letter.txt", 'r') as f:
    letter_text = f.read()

names = []
with open("./Input/Names/invited_names.txt", "r") as f:
    names = f.read().splitlines()

for n in names:
    with open(f'./Output/ReadyToSend/{n}.txt', 'w') as f:
        f.write(letter_text.replace('[name]', n))
