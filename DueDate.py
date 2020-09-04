current_hour = 12
current_minute = 37
current_section = "PM"
due_hour = 9
due_minute = 0
due_section = "AM"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Given the current time and deadline time represented by the
#variables above, determine if an assignment is still eligible
#for submission. An assignment is eligible if the time
#represented by current_hour, current_minute, and
#current_section is before the time represented by due_hour,
#due_minute, and due_section.


#Add your code here!

# translate everything into minutes
current_time = ((current_hour % 12) + (12 * (current_section == "PM"))) * 60 + current_minute
due_time = ((due_hour % 12) + (12 * (due_section == "PM"))) * 60 + due_minute
print(current_time < due_time)

