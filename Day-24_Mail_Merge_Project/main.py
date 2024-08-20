# Making a list of names
with open("D:/Raghav soni/Git Files/Python_100_Days_of_Code_Projects/Day-24_Mail_Merge_Project/Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

for name in names:
    # Removing '\n' from names
    txt = name.strip()
    with open(f"D:/Raghav soni/Git Files/Python_100_Days_of_Code_Projects/Day-24_Mail_Merge_Project/Output/letter_for_{txt}.docx", "w") as file:
        with open("D:/Raghav soni/Git Files/Python_100_Days_of_Code_Projects/Day-24_Mail_Merge_Project/Input/Letters/starting_letter.txt") as starting_letter:
            letter = starting_letter.read()
            # Replacing name and putting original name
            letter = letter.replace("[name]", txt)
            file.write(letter)
