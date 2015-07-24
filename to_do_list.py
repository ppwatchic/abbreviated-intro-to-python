"""
Let's create a to do list. I know, thrilling. 
Ask the user for 5 items to put into their to do list.
Once the user has provided 5 items, display the list back
to the user.
"""

print "Greetings Busy Bee! Let's get to work making that TO DO list!"
my_to_dos = []

list_len = 5

# HINT: You can see how many items are in the 
# list by using the built-in function len!
# Example: len(my_to_dos)

# Now ask for user input, and remember we want **5 items**!!!
# How can we repeat asking the user to give us all the items?
while 1:
	my_to_dos.append(raw_input("Please type in your to-do-list: > "))
	if len(my_to_dos) > 4 :
		break
	

print "Fantastic! Here is the list of things you have to do today:"
for item in my_to_dos: 
	print item

# Again, how can we repeat something? But this time
# it doesn't have to be tied to a specific condition. 
# We just want to see everything in our list.
