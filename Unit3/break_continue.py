'''
Break and Continue Lesson in CodeHS
'''

while True:
    x = int(input("Number: "))
    if x > 0:
        break #exits the loop after this line
    else:
        continue #returns to the top of the loop

print("You chose",x)

for i in range(15):
    if x == 7:
        break
    else:
        continue
print("You found 7")

##Printing on a single line
for i in range(6):
    print(str(i),end = "\t")

print("")
for i in range(5):
    print(str(i),end = "--")
print(5) #this is how I can avoid the - at the end
