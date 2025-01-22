# Whule loops. A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement. The code inside the loop will be executed as long as the Boolean expression evaluates to True. the while loop is used when the number of iterations is not known before the first iteration begins. The condition is evaluated before the execution of the loop’s body. If the condition is False, the loop body will not be executed at all.
count=0
while count <= 3:
   # Loop Body
   print(count)
   count += 1
   # Any other code at this level of indentation will
   # run on each iteration


  # While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Your code below: 
countdown = 10
while countdown >=0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")

#While for lists. While loops can be used to iterate through lists, just like for loops. The difference is that while loops are used when the number of iterations is not known before the first iteration begins. The condition is evaluated before the execution of the loop’s body. If the condition is False, the loop body will not be executed at all. When using a while loop to iterate through a list, it’s a good idea to include a counter variable to keep track of the current index. This is because while loops require explicit incrementing and decrementing of the counter variable. Without a counter variable, it’s easy to end up with an infinite loop. When using a while loop to iterate through a list, it’s a good idea to include a counter variable to keep track of the current index. This is because while loops require explicit incrementing and decrementing of the counter variable. Without a counter variable, it’s easy to end up with an infinite loop. 
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0
while index < length:
  print("I am learning about " + python_topics[index])
  index += 1
