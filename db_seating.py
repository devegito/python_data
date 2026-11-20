squad_size = int(input("How many fighters are in your group? "))
if squad_size > 8:
    print("You are " + str(squad_size) + " people! You'll have to wait for a table.")
else:
    print("You are " + str(squad_size) + " people! Your table is ready!")