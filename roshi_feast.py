prompt = "\nRoshi: Enter the food you want to have."
prompt += "\nRoshi: Or tell me 'Im full!' if you don't want to have more food: "
food = ""
while food != "Im full!":
    food = input(prompt)
    if food != "Im full!":
        print(f"Roshi: {food.title()} coming right up!")
print(f"Roshi: Woah! you eat alot Goku!")
print(f"Roshi: Thanks for coming, Bye now!")