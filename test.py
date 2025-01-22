numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    continue
  print(number)
  
  time = "3pm"
mood = "good"

def report():  # sourcery skip: use-fstring-for-concatenation
  print("The current time is " + time)
  print("The mood is " + mood)

print("Beginning of report")

report()

quantity_one = 5
quantity_Two = 7

print(quantity_one < 4 or quantity_Two < 6)
