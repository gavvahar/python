transportation = []
car = ''
while car != 'q':
    car = input('Please enter a car name ')
    transportation.append(car)
transportation.remove('q')

for x in transportation:
    print(x.title())
