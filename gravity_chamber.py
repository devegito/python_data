chamber_active = True
prompt = "\nEnter Vegeta's training move (or 'off' to stop the chamber): "

while chamber_active:
    command = input(prompt)
    if command == 'quit':
        chamber_active = False
    else:
        print(f"Vegeta executes: {command}!")
print("Vegeta is done training... Time to rest!")