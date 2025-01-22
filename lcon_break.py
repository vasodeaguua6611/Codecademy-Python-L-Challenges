# Loop Control: Break. The break statement is used to exit a loop early. It is often used in loops that run indefinitely, or when the loop has already run its course and the remainder of the iterations are unnecessary. The break statement can be used in both while and for loops. When the break statement is executed, the loop will immediately terminate. The program will continue to execute the code that follows the loop. The break statement is often used with an if statement to test for a certain condition and only break out of the loop if that condition is met. The break statement is often used with an if statement to test for a certain condition and only break out of the loop if that condition is met.

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"
for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
   print("They have the dog i want!")
   break





#LOOPCONTROL = CONTINUE. While the break control statement will come in handy, there are other situations where we don’t want to end the loop entirely. What if we only want to skip the current iteration of the loop? For this, we use the continue statement. The continue statement is used to skip the current iteration of the loop and continue with the next iteration. It can be used in both while and for loops. When the continue statement is executed, the loop will skip the remaining code in the loop’s body and move on to the next iteration. The continue statement is often used with an if statement to test for a certain condition and only continue with the loop if that condition is met. The continue statement is often used with an if statement to test for a certain condition and only continue with the loop if that condition is met. When the continue statement is executed, the loop will skip the remaining code in the loop’s body and move on to the next iteration.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
    if age < 21:
        continue
    print(age)


#List comprehensions
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for digit in single_digits:
  print(digit)
  squares.append(digit ** 2)
print(squares)
cubes = [di ** 3 for di in single_digits]
print(cubes)