motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(0, 'ducati')
del motorcycles[2]
del motorcycles[0]
print(motorcycles[-1])

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
