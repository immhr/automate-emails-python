with open("./input/letters/starting_letter.txt", "r") as file_open:
    content = file_open.read()

with open("./input/Names/invited_names.txt", "r") as invited_names:
    names = invited_names.read().split("\n")

    for name in names:
        with open(f"output/ReadyToSend/LetterTo{name}", "w") as LetterToInvites:
            individual_letter = LetterToInvites.write(content.replace("[name]", name))
