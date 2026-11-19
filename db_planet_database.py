planets = {
    'Namek' : {
        'Race' : 'Namekians',
        'Status' : 'Destroyed'
    },
    'Earth' : {
        'Race' : 'Humans/Saiyans',
        'Status' : 'Active'
    }
}
for planet, info in planets.items():
    print("\nPlanet Name: " + planet)
    print("\tRace: " + info['Race'])
    print("\tStatus: " + info['Status'])