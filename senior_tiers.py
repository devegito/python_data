power = -1

if power < 1000:
    tier = "Weakling"
elif power < 5000:
    tier = "Average Fighter"
elif power <= 9000:
    tier = "Strong Warrior"
else:
    tier = "It's over 9000!"

print("Tier: " + tier)