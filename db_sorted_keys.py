tournament_roster = {
    'Vegeta' : 8500,
    'Goku' : 9000,
    'Piccolo' : 3000,
    'Gohan' : 2500
}
for name in sorted(tournament_roster.keys()):
    print("Welcome to the tournament, " + name.title() + "!")
