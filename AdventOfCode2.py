f = open("Input/input2.txt", "r")

vertical=0
horizontal=0
aim=0
commands=[]
for x in f:
    commands.append(x)

for command in commands[::1]:
    strCommand=command.split(" ")[0]
    unit=int(command.split(" ")[1])

    if strCommand=="forward":
        horizontal=horizontal+unit
        vertical = vertical + (aim *unit)
    elif strCommand=="down":
        #vertical = vertical+unit
        aim = aim + unit
    elif strCommand == "up":
        aim = aim - unit
        #vertical = vertical - unit


print(vertical)
print(horizontal)
print(vertical*horizontal)
f.close()