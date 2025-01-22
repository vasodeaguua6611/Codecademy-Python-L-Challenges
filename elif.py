#We have if statements, we have else statements, we can also have elif statements.
#Elif stands for else if. It allows us to check multiple conditions.
#Now you may be asking yourself, what the heck is an elif statement? It’s exactly what it sounds like, “else if”. An elif statement checks another condition after the previous if statements conditions aren’t met. We can use elif statements to control the order we want our program to check each of our conditional statements. First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.
#exampol 

donation = 300
print("Thank you for the donation!")

if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")


#PROYECTITO 
#Calvin Coolidge’s Cool College has noticed that students prefer to get letter grades. Help them set up a grade system.

grade = 86
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")