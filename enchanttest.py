import enchant
d = enchant.Dict("en_US")
if (d.check("Hello")):
    print("True")