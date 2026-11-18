power_levels = {
    'Goku' : 9000,
    'Vegeta' : 9000,
    'Piccolo' : 3000,
    'Gohan' : 3000
}

print("The unique power levels on the battlefield are:")

for power in set(power_levels.values()):
    print(power)
    