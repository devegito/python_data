unconfirmed_fighters = ['chiaotzu', 'tien', 'yamcha']
confirmed_fighters = []

while unconfirmed_fighters:
    current_fighter = unconfirmed_fighters.pop()
    print(f"King Kai is verifying: {current_fighter.title()}")
    confirmed_fighters.append(current_fighter)

print("\nThe following fighters are approved for King Kai's training:")
for confirmed_fighter in confirmed_fighters:
    print(confirmed_fighter.title())