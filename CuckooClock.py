current_hour = 5
time_of_day = "PM"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write some code that will print the following message based
#on the values of current_hour and time_of_day:
#
#The current time is 5PM: Cuckoo!Cuckoo!Cuckoo!Cuckoo!Cuckoo!
#
#The values of current_hour and time_of_day should replace
#"5PM", and "Cuckcoo!" should be printed current_hour times.
#
#For example, if current_hour was 2 and time_of_day was "AM",
#this would print:
#
#The current time is 2AM: Cuckoo!Cuckoo!


#Add your code here!
current_hour_as_str = str(current_hour)
actual_time = current_hour_as_str + time_of_day 
cuckoo = "Cuckoo!" * current_hour

print("The current time is " + actual_time + ": " + cuckoo)

