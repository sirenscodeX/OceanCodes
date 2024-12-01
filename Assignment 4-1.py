charge = 0.00
numChars = 8
color = "gold"
woodType = "oak"
if numChars < 10:
    charge = 40
else:
    charge = 40 + (numChars - 10) * 5
    print("The charge for this sign is $", charge)
    charge = 0.00
    numChars = 8
    color = "gold"
    woodType = "oak"
    if woodType == "oak":
        charge = 40 + (numChars * 5)
    else:
        charge= 40 + (numChars * 4)
        print("The charge for this sign is $", charge)
        charge = 0.00
        numChars = 20
        color = "gold"
        woodType = "pine"
        if woodType == "oak":
            charge = 40 + (numChars * 5)
        elif woodType == "pine":
            charge = 40 + (numChars * 4)
        else:
            charge = 40 + (numChars * 3)
            print("The charge for this sign is $, charge")
            charge = 0.00
            numChars = 18
            color = "black"
            woodType = "oak"
            if woodType == "oak":
                charge = 40 + (numChars * 5)
            elif woodType == "pine":
                charge = 40 + (numChars * 4)
            else:
                charge = 40 + (numChars * 3)
                print("The charge for this sign is $", round(charge,2))