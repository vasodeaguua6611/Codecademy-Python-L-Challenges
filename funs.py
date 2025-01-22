#Functions. Functions are a way to organize code in Python. They are reusable code blocks that can be called multiple times.
#Functions are defined using the def keyword followed by the function name and parentheses ().
#The code block within every function starts with a colon (:) and is indented.
#Functions can return data using the return keyword followed by the data to return.
#Functions can accept arguments, which are input values passed into the function.
#Arguments are defined within the parentheses following the function name.
#Arguments are separated by commas.
#Functions can have default arguments with default values specified after the equals sign (=).
#Default arguments are used when no argument is specified.
#Functions can accept a variable number of arguments using the *args parameter.
#The *args parameter allows the function to accept any number of positional arguments.

#Ex
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")

#Multiple parameters
#Multiple parameters can be passed to a function by separating them with commas. The order of the parameters must match the order of the arguments passed to the function.
# Ex
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
 
  return trip_total
  
print(calculate_expenses(200, 100, 100, 5))

# Return arguments. Return statements are used to return data from a function. The return keyword is followed by the data to return.
# The return statement can be used to return any data type, including strings, integers, and lists. 
# If the return statement is followed by a value, the function will return that value. If the return statement is not followed by a value, the function will return None.
# Ex

current_budget = 3500.75

def print_remaining_budget(budget):
  print(f"Your remaining budget is: ${budget}")

def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)

# Multiple return statements. Functions can have multiple return statements. The return statement can be used to return different values based on conditions.
# Sometimes we may want to return more than one value from a function. We can return several values by separating them with a comma.                
# Ex
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third 
  
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)


# Review
# Excellent work! 👏 In this lesson, you’ve covered a major fundamental programming concept used in the majority of all programs to organize code into reusable blocks. To recap, we explored:
# 
# What problems arise in our programs without functions
# What functions are and how to write them
# How whitespace plays an important role in how a program will execute our code and more importantly distinguish function code from non-function code
# How to pass input values into our functions using parameters and arguments
# The difference between built-in and user-defined functions and some common built-in functions python offers
# How we can reuse function output with the return keyword, as well as multiple returns.
# Where variables can be accessed in our programs that use functions
# Ex
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("pipis")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(7.5)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
    print("Your trip starts off in " + origin)
    print("And you are travelling to " + destination)
    print("You will be traveling by " + mode_of_transport)
    print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Italy", "Peru", estimate, "Car")