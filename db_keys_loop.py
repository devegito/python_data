scouter_data = {
    'goku' : 9000,
    'vegeta' : 8500,
    'piccolo' : 3000
}
vip_fighters = ['goku', 'vegeta']
for name in scouter_data.keys():
    print(name.title())
    if name in vip_fighters:
        print(name.title() + " has the power level of " + str(scouter_data[name]))
if 'Broly' not in scouter_data.keys():
    print("Broly is missing from the roster!")