last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# This semester's Gradebook rahhh: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Subjects + Grades
subjects_grades = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]
gradebook= subjects_grades
# print(gradebook) (Not usable anymore)

# Your grade for your computer science class just came in! You got a perfect score, 100
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 98])
#print(gradebook)

# Let's switch from a numerical grade value to a Pass/Fail option for our poetry class. Because we are that masochistic
gradebook[2].remove(85)
gradebook[2].append("Pass")

# And now, the entire year, RAHHHH
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)

