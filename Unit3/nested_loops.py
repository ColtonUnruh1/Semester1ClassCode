"""
Name: Brandon Smith
Date: 10/11/23
File name: nested_loops.py
Description: Lesson on nested loops
"""

#write a while loop that prints the number 1-10 on a single line
#with spaces inbetween
num = 1
while num < 11:
    print(num,end = ' ')
    num = num + 1
print('')

#write a for loop " "
for i in range(1,11):
    print(i, end = ' ')

#write a for loop that prints "bookshelf" twelve times
#each on a new line
print('')

for i in range(12):
    print("bookshelf")

count = 0
for i in range(6):
    for j in range(2):
        count = count + 1
        print(str(count)+" bookshelf")

#make a 5x5 multiplication table
# 1 2  3  4  5
# 2 4  6  8  10
# 3 6  9  12 15
# 4 8  12 16 20
# 5 10 15 20 25

for row in range(1,6):
    for column in range(1,6):
        print(row*column,end='\t')
    print('')
print('')
for row in range(1,6):
    column = 1
    while column < 6:
        print(row*column,end = "\t")
        column = column + 1
    print('')
