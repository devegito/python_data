enemies = [
    'saibaman',
    'nappa',
    'saibaman',
    'vegeta',
    'saibaman'
]
print(f"Enemies on battlefield: {enemies}")
while 'saibaman' in enemies:
    print(f"Goku defeats a Saibaman!")
    enemies.remove('saibaman')
print(f"Remaining bosses: {enemies}")