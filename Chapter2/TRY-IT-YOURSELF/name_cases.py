person = 'Eric'
ls1 = [person.lower(), person.upper(), person.title()]
ls2 = ['lower case', 'upper case', 'title form']
x = 0
while x < len(ls1):
    print(
        f"Hello {ls1[x]}, would you like to learn some Python today? - {person} is in {ls2[x]}")
    x = x + 1
