person = input("How old are you? ")
intPerson = int(person)
if intPerson < 2:
    print("You are a baby")
elif intPerson >= 2 and intPerson < 4:
    print("You are a toddler")
elif intPerson >= 4 and intPerson < 13:
    print("You are a kid")
elif intPerson >= 13 and intPerson < 20:
    print("You are a teenager")
elif intPerson >= 20 and intPerson < 65:
    print("You are an adult")
else:
    print("You are an elder")
