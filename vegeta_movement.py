vegeta = {}

vegeta['x_position'] = 0
vegeta['speed'] = 'medium'
print("Starting X position: " + str(vegeta['x_position']))

if vegeta['speed'] == 'slow':
    x_increment = 1

elif vegeta['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3

vegeta['x_position'] = vegeta['x_position'] + x_increment

print("New X position: " + str(vegeta['x_position']))

vegeta['speed'] = 'fast'

if vegeta['speed'] == 'slow':
    x_increment = 1

elif vegeta['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3

vegeta['x_position'] = vegeta['x_position'] + x_increment

print("Super Saiyan X position: " + str(vegeta['x_position']))