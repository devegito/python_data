prompt = "\n--- Scouter Communication Channel ---"
prompt += "\nEnter battle command for Vegeta (or 'rest' to turn off scouter): "

command = ""
while command != 'rest':
    command = input(prompt)
    if command != 'rest':
        print("Transmitting to Vegeta: " + command + ".")