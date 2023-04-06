gl = ['Bob', 'Rob', 'Tom']
for x in gl:
    print(f"{x}, you have been invited to dinner a TGIF at 8PM")
print(f"{len(gl)} people has been invited")

print(" ")

notComing = []
answer = ''
for t in gl:
    answer = input(f"{t} can you make it to dinner? Type yes or no. ")
    if answer.lower() == 'no':
        element = t
        index = gl.index(element)
        notComing = notComing[:index] + [element]+notComing[index:]

print(" ")

for ls in notComing:
    print(
        f"It looks like {ls} isn't going to be able to make it for the dinner")
    gl.remove(ls)

print(" ")

for x in gl:
    print(f"{x} even though {notComing} won't be able to make it you are still invited.")

count = 0
while count < len(gl):
    del gl[0]
print(gl)
