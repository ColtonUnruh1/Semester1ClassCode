'''
Name: Mr. Smith
Date: 9/7/23
Assignment: Rectangle Calculator
Description: This program will ask a user for a
length and width. It will then calculate the area
and perimeter and print both.

'''

#Ask the user for the length and store in rect_length
rect_length = int(input("Enter a length: "))
#Ask the user for the width and store in rect_width
rect_width = int(input("Enter a width: "))
#Calculate the area and store in rect_area
rect_area = rect_length * rect_width
#Calculate the perimeter and store in rect_perimeter
rect_perimeter = 2 * (rect_length + rect_width)
#Print the area and perimeter
print("The rectangle with a width of",rect_width,"and a length of",
      rect_length,"has a perimeter of",rect_perimeter,"and an area of",
      rect_area,".")
