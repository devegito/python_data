prompt = "\nEnter a planet name for Goku to visit:"
prompt += "\nEnter 'stop' to end the planet search: "

while True:
    planet = input(prompt)
    if planet == 'stop':
        break
    else:
        print(f"Goku instantly teleports to {planet.title()}!")

print("Planet search has ended... Goku teleports back to Earth!")