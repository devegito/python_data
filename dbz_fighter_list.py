goku = {
    'Name' : 'Goku',
    'Race' : 'Saiyan'
}
vegeta = {
    'Name' : 'Vegeta',
    'Race' : 'Saiyan'
}
piccolo = {
    'Name' : 'Piccolo',
    'Race' : 'Namekian'
}
roster = [goku, vegeta, piccolo]

for fighter in roster:
    print(fighter['Name'] + " is a " + fighter['Race'] + ".")