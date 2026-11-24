wishes = {}
wish_polling = True
while wish_polling:
    name = input("\nWhat is your name, Z-Fighter? ")
    wish = input("State your wish! ")
    wishes[name] = wish
    repeat = input("Is another fighter making a wish? (y/n): ")
    if repeat == 'n':
        wish_polling = False
print("\n--- 🐉 Shenron's Wish Registry Results ---")
for name, wish in wishes.items():
    print(f"{name.title()} wished for: {wish}!")