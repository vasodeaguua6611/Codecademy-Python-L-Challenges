#Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. In these cases, you can build larger boolean expressions using boolean operators. These operators (also known as logical operators) combine smaller boolean expressions into larger expressions. There are three boolean operators in Python: and, or, and not. 

# AND. 

(1 + 1 == 2) and (2 + 2 == 4)   # True

(1 > 9) and (5 != 6)            # False

(1 + 1 == 2) and (2 < 1)        # False

(0 == 10) and (1 + 1 == 1)      # False

#Let’s return to Calvin Coolidge’s Cool College. 120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher. Rewrite the if statement so that it checks to see if a student meets both requirements using an and statement.

credits = 120
gpa = 3.4

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
  
  
  # OR.
  # Este esta mas tranca. asi q voy a pastear la expli de codecademy. The boolean operator or combines two expressions into a larger expression that is True if either component is True. If both components are False, then the expression is False. 
  
  True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

#Let's go back to Calvin Coolidge’s Cool College. This time, a student will graduate if they have 120 or more credits or a GPA of 2.0 or higher. Rewrite the if statement so that it checks if a student meets either requirement using an or statement.

credits = 118
gpa = 2.0

if (credits >= 120) or (gpa >= 2.0):
    print("You have met at least one of the requirements.")
    
    
# NOT. 
#The final boolean operator we will cover is not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement. If we have a False statement and apply a not operator we get a True statement.

not 1 + 1 == 2  # False
not 7 < 0       # True

#Let's go back to Calvin Coolidge’s Cool College. This time, a student will graduate if they have 120 or more credits and a GPA of 2.0 or higher. Rewrite the if statement so that it checks if a student does not meet both requirements using a not statement.

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
    print("You do not meet either requirement to graduate!")
    #CC