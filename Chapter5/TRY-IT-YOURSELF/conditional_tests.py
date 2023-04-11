carList = {'lexus', 'subaru', 'ford', 'nissan', 'tesla',
           'rivian', 'porsche', 'ferrari', 'dodge', 'lamborghini'}
car = {'subaru', 'lexus', 'porsche', 'ferrari', 'tesla'}
newList1 = carList.intersection(car)
for x in newList1:
    print(f"Is car == '{x}'? I predict True.")
    print(car == x)

newList2 = carList.difference(car)
for x in newList2:
    print(f"\nIs car == '{x}'? I predict False.")
    print(car == x)
