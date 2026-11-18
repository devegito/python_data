# --- PART 1: MOVES ---

fighter_moves = {
    'Goku' : 'Kamehameha',
    'Vegeta' : 'Final Flash',
    'Piccolo' : 'Special Beam Cannon'
}
for name, move in fighter_moves.items():
    print(name.title() + " uses the " + move.title() + ".")

# --- PART 2: PLANETS ---
fighter_planets = {
    'Goku' : 'Earth',
    'Vegeta' : 'Planet Vegeta',
    'Piccolo' : 'Namek'
}
for name, planet in fighter_planets.items():
    print(name.title() + " is on the roster.")
for planet in set(fighter_planets.values()):
    print("The following planets are represented: " + planet.title())

# --- PART 3: LIST ---
registered_fighters = {
    'Goku' : 'Yes',
    'Vegeta' : 'Yes'
}
arrivals = [
    'Goku',
    'Piccolo',
    'Vegeta',
    'Gohan'
]
for arrival in arrivals:
    if arrival in registered_fighters:
        print("Thank you for registering " + arrival + "!")
    else:
        print(arrival + ", you still need to register!")