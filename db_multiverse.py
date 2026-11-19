multiverse = {
    'Universe 7' : {
        'God' : 'Beerus',
        'Angel' : 'Whis',
        'Top Fighter' : 'Goku'
    },
    'Universe 6' : {
        'God' : 'Champa',
        'Angel' : 'Vados',
        'Top Fighter' : 'Hit'
    }
}
for universe_name, info in multiverse.items():
    print("\nUniverse: " + universe_name)
    print("\nGod: " + info['God'])
    print("\nAngel: " + info['Angel'])
    print("\nTop Fighter: " + info['Top Fighter'])