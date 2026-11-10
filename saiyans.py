saiyans=['Goku','Vegeta','Cabba']
print(saiyans)
for saiyan in saiyans:
    print(saiyan + " is a pure blooded Saiyan.\n")
print("None of them is a hybrid.")
friend_saiyans=saiyans[:]
saiyans.append("Broly")
friend_saiyans.append("Kale")
print("My Saiyans are:")
for saiyan in saiyans:
    print(saiyan)
print("\nMy friend's Saiyans are:")
for saiyan in friend_saiyans:
    print(saiyan)