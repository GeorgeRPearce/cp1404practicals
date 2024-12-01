CODE_TO_NAME = {"biyzantne": "#bd33a4", "camel": "#c19a6b", "black": "#000000",
                "aqua": "#00ffff", "aliceblue": "f0f8ff", "cardinal": "#c41e3a",
                "celadon": "#ace1af", "celeste": "#b2ffff", "cobalt": "#0047ab",
                "cinnabar": "#e34234"}

print(CODE_TO_NAME)

colour_name = input("What colour: ").lower()
while colour_name != "":
    if colour_name in CODE_TO_NAME:
        print("{:9}".format(colour_name), "is", CODE_TO_NAME[colour_name])
    else:
        print("Invalid colour")
    colour_name = input("What colour: ").lower()
