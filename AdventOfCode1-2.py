f = open("Input/input1.txt", "r")

counter =0
counterScore=0
numbers=[]
for x in f:
    numbers.append(int(x))

for number in numbers[::1]:
    listA=numbers[0+counter:3+counter:]
    listB = numbers[1+counter:4+counter:]

    sumA= sum(listA)
    sumB = sum(listB)

    if(sumB>sumA):
        counterScore+=1

    counter+=1

print(counterScore)
f.close()