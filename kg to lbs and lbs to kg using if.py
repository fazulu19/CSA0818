weight = float(input("weight"))
unit = input ("(k)g or (L)bs: ")
if unit.upper() == "K":
    convert = weight /0.45
    print("weight in lbs: " + str(convert))
else:
              convert = weight*0.45
              print("weight in KG" + str(convert))
