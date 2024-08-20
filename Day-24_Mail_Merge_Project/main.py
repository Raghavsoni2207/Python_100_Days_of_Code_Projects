# Making a list of names
with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

for name in names:
    # Removing '\n' from names
    txt = name.strip()
    with open(f"./Output/letter_for_{txt}.docx", "w") as file:
        with open("./Input/Letters/starting_letter.txt") as starting_letter:
            letter = starting_letter.read()
            # Replacing name and putting original name
            letter = letter.replace("[name]", txt)
            file.write(letter)
