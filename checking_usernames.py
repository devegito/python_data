current_users = ['goku', 'vegeta', 'piccolo', 'gohan', 'trunks']
new_users = ['Goku', 'Gohan', 'Broly', 'Frieza', 'Piccolo']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry, that name is already taken.")
    else:
        print("That username is available.")