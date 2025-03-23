#Jonah Aney, Jan. 26, 2025 CSD205 Module: 4.2 Miles to Kilometers Conversion

#citations:
# Goyal, S. (2024, April 16). Python Program To Convert Kilometers To Miles (+Detailed Examples).
# Unstop.com. Retrieved January 26, 2025, from https://unstop.com/blog/python-program-to-convert-kilometers-to-miles  #not the exact conversion, but it provided insight to the approach of the program
#js6seaj47. r/learningpython. Still struggling with programming. https://www.reddit.com/r/learnpython/comments/q2tmo1/still_struggling_with_programming/?share_id=uoAS_qU6wvibZw5B6YkVD&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=10


def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

#ask the user for the number of miles driven. Create a variable to hold this value.
#using try/except keywords to handle input.
try:
    miles = int(input('Enter the number of miles: '))
except ValueError:
    print('Invalid input. Please enter a valid number.')
    exit()
return()miles
#call the function to convert the input value and then hold the converted value in the variable 'kilometers'
kilometers = miles_to_kilometers(miles)

#display the number of miles and kilometers using both variables in your program.
print(f'You have driven {miles} miles. That is equal to {kilometers} kilometers.')


