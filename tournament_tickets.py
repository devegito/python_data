prompt = "\nTicket seller: Welcome to The 24th World Martial Arts Tournament!"
prompt += "\nTicket seller: Please mention your age to buy a ticket! :"

active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Ticket seller: Ticket is free for toddlers!")
        elif age <=12:
            print("Ticket seller: That will be 10 Zeni please!")
        else:
            print("Ticket seller: That will be 15 Zeni please!")

print("Ticket seller: Thanks for coming to World Martial Arts Tournament!")
print("Have a nice day!")
        