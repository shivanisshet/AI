
room = {
    "A": input("Enter status of Room A (Clean/Dirty): ").upper(),
    "B": input("Enter status of Room B (Clean/Dirty): ").upper()
}

position = input("Enter vacuum position (A/B): ").upper()

for i in range(4):
    print("\nCurrent Room:", position)
    print("Room A:", room["A"])
    print("Room B:", room["B"])

    if room[position] == "DIRTY":
        print("Action: SUCK")
        room[position] = "CLEAN"
    else:
        print("Action: MOVE")

        if position == "A":
            position = "B"
        else:
            position = "A"

print("\nFinal State:")
print("Room A:", room["A"])
print("Room B:", room["B"])