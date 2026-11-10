usernames = []

if usernames:
    for username in usernames:
        if username == 'Beerus':
            print("Hello Lord Beerus, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")