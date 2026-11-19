fighter_moves = {
    'Goku' : ['Kamehameha', 'Spirit Bomb'],
    'Vegeta' : ['Final Flash', 'Galick Gun'],
    'Piccolo' : ['Special Beam Cannon', 'Hellzone Gernade']
}
for name, moves in fighter_moves.items():
    print("\n" + name + "'s moves:")
    for move in moves:
        print("\t" + move)