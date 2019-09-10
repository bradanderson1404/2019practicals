HEX_COLOURS = {"Cyan1": "#00ffff", "BlueViolet": "#8a2be2", "DarkSeaGreen": "#8fbc8f", "FireBrick2": "#ee2c2c",
               "GhostWhite": "#f8f8ff", "GreenYellow": "#adff2f", "HotPink": "#ff69b4",
               "Lavender": "#e6e6fa", "NavyBlue": "#000080", "Wheat1": "#ffe7ba"}

for key in HEX_COLOURS:
    print("{:>12s} is {}".format(key, HEX_COLOURS[key]))

colour = input("\nEnter colour name: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour name")
    colour = input("\nEnter colour name: ")
