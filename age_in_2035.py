"""
ITERATION ONE: 
Write a program that displays your first name and age today in 2015.
The program should also dispaly your age in 2035.

Provided is some code showing you how to start.
"""

name = "Pingping"
age_today = 31
print name + " is " + str(age_today) + " years old today."
# TODO: Find how many years from now 2035 is, update age_today with difference in years.
# Display this to the user.
year_future = 2035 
year_now = 2015
age_future = age_today + year_future - year_now
print name + " will be " + str(age_future) + " years old in " + str(year_future)

"""
ITERATION TWO: 
Write a program that asks the user for their first name and age.
The program should also display this information as well as the 
user's age in 2035.

Use the raw_input function to help you take input.
"""

# TODO: Now use raw_input!
print "Please type in your first name: "
first_name = raw_input("> ")
print "Good to know your name," + first_name + ". You will be " + str(age_future) + "years old in" + str(year_future)

