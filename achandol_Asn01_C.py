'''
CS1026a 2023
Assignment 01 Project 01 - Part C
Krish Chandola
251371956
October 4th 2023
'''

print("project One <01> Part C: The Moore the Merrier ")

# Ask for input
Transistors = int(input("Starting number of transistors: "))
YearN = int(input("Starting year: "))
Years = int(input("Total number of year: "))

# Since each year is 2 years apart divide the number of years by two
LoopNumber = Years//2

# Determine the number of flops based on the formula given
Flops = Transistors * 50

# Display the flops in unit definition by making it so any number above a 1000 and 1000000 is shown in unit definition
# This is done before the loop as the first line is not part of the loop because that is what the user has inputted
UDFlops = float(Transistors * 50)
if UDFlops >= 10 ** 24:
    print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 24:.2f} YottaFLOPS {Flops:,}")
elif UDFlops >= 10 ** 21:
    print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 21:.2f} ZettaFLOPS {Flops:,}")
elif UDFlops >= 10 ** 18:
    print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 18:.2f} ExaFLOPS {Flops:,}")
elif UDFlops >= 10 ** 15:
    print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 15:.2f} PetaFLOPS {Flops:,}")
elif UDFlops >= 10 ** 12:
    print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 12:.2f} TeraFLOPS {Flops:,}")
elif UDFlops >= 10 ** 9:
    print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 9:.2f} GigaFLOPS {Flops:,}")
elif UDFlops >= 1000000:
    print(f"{YearN} {Transistors:,} {UDFlops / 1000000:.2f} MegaFLOPS  {Flops:,} ")
elif UDFlops >= 1000:
    print(f"{YearN} {Transistors:,} {UDFlops / 1000:.2f} KiloFLOPS {Flops:,}")
else:
    print(f"{YearN} {Transistors:,} {UDFlops:.2f} FLOPS  {Flops:,} ")

# Start the loop using range
for i in range(LoopNumber):
    # Multiply and add the transistors and the year number
    Transistors *= 2
    YearN += 2
    # Flops formula in the loop
    Flops = Transistors * 50

# Unit Definition in the loop
# Display the numbers
    UDFlops = float(Transistors * 50)
    if UDFlops >= 10 ** 24:
        print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 24:.2f} YottaFLOPS {Flops:,}")
    elif UDFlops >= 10 ** 21:
        print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 21:.2f} ZettaFLOPS {Flops:,}")
    elif UDFlops >= 10 ** 18:
        print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 18:.2f} ExaFLOPS {Flops:,}")
    elif UDFlops >= 10 ** 15:
        print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 15:.2f} PetaFLOPS {Flops:,}")
    elif UDFlops >= 10 ** 12:
        print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 12:.2f} TeraFLOPS {Flops:,}")
    elif UDFlops >= 10 ** 9:
        print(f"{YearN} {Transistors:,} {UDFlops / 10 ** 9:.2f} GigaFLOPS {Flops:,}")
    elif UDFlops >= 1000000:
        print(f"{YearN} {Transistors:,} {UDFlops / 1000000:.2f} MegaFLOPS  {Flops:,} ")
    elif UDFlops >= 1000:
        print(f"{YearN} {Transistors:,} {UDFlops / 1000:.2f} KiloFLOPS {Flops:,}")
    else:
        print(f"{YearN} {Transistors:,} {UDFlops:.2f} FLOPS  {Flops:,} ")
print("END: Project One <01> - Part C")
print("Krish Chandola    Achandol    251371956")