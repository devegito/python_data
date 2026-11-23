prompt = "\nRoshi: Enter the food you want to have."
prompt += "\nRoshi: Or tell me 'full' to stop eating: "

while True:
    food = input(prompt)
    if food == 'full':
        break
    else:
        print(f"Roshi: {food.title()} coming right up!")
print("Roshi: You ate so much! Goodbye!")