with open("Input/Letters/starting_letter.txt", mode="r") as template:
    with open("Input/Names/invited_names.txt", mode="r") as names:
        template_letter = template.read()
        content = names.read()
        name = content.split("\n")
        for n in name:
            new_letter = template_letter.replace("[name]", n)
            with open(f"Output/ReadyToSend/Letter_to_{n}.txt", mode="w") as letter_to:
                letter_to.write(new_letter)
