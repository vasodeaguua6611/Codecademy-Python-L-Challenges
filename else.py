#else statements allow us to elegantly describe what we want our code to do when certain conditions are not met.
#else statements are used to execute code when the if condition is not met.
#EXAMPLE
weekday = True
if weekday:
  print("wake up at 6:30")
else:
  print("sleep in")

#PROPOR
# Calvin Coolidge’s Cool College has another request for you. They want you to add an additional check to a previous if statement. If a student is failing to meet one or both graduation requirements, they want it to print:
# "You do not meet the requirements to graduate."

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate")