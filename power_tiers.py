power = 9001

if power < 1000:
    tier = "Weakling"
elif power < 9000:
    tier = "Strong Fighter"
else:
    tier = "Over 9000!"

print("This fighter's power tier is: " + tier)