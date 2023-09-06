'''
Write a program that asks a user for the length
and width of a rectangle and then prints the
perimeter and area of that rectangle.
'''
rect_length = int(input("Enter the length of a rectangle: "))
rect_width = int(input("Enter the width of a rectangle: "))

rect_area = rect_length * rect_width
rect_perimeter = 2*rect_length + 2*rect_width

print("The area of that rectangle is",rect_area)
print("The perimeter of that rectangle is",rect_perimeter)
