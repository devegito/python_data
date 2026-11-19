# --- PART 1 MANUAL WAY ---
goku = {
    'Power Level' : 9000,
    'Form' : 'Base Form'
}
vegeta = {
    'Power Level' : 8500,
    'Form' : 'Base Form'
}
piccolo = {
    'Power Level' : 3000,
    'Form' : 'Base Form'
}
z_fighters = [goku, vegeta, piccolo]
for z_fighter in z_fighters:
    print(z_fighter)

# --- PART 2 AUTOMATED ARMY ---

saibaman_army = []
for saibaman in range(10):
    new_saibaman = {
        'Color' : 'Green',
        'Power' : 1200
    }
    saibaman_army.append(new_saibaman)
    print(saibaman_army[:3])
    print(len(saibaman_army))

    # --- PART 3 THE UPGRADE ---

    for saibaman in saibaman_army[:5]:
        if saibaman['Color'] == 'Green':
            saibaman['Color'] = 'Yellow'
            saibaman['Power'] = 2500
    for saibaman in saibaman_army[:5]:
        print(saibaman)