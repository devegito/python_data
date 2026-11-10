available_techniques = ['Kamehameha', 'Spirit Bomb', 'Final Flash']
requested_techniques = ['Kamehameha', 'Destructo Disc', 'Final Flash']

for technique in requested_techniques:
    if technique in available_techniques:
        print(technique + " is available for use!")
    else:
        print("Sorry, we don't have " + technique + " available.")
        