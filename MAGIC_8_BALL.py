# Magic 8-Baller! Your cheap, questionable and not so credible fortune teller! 
# Imput your name and question, and the Magic 8-Baller will give you an answer! Don't be shy, ask away!

import random

name = "Pimpi"
question = "Am i real?"
answer = ""
random_number = random.randint(1,15)

print(random_number)

if random_number == 1:
    answer = "Yes-definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later :)"
elif random_number == 6:
    answer = "Oof, better not tell you now"
elif random_number == 7:
    answer = "My sources say...no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "How the hell do you expect me to answer that? I predict the future, but i don't know everything, you pretentious brat"
elif random_number == 11:
    answer = "Maybe, maybe not. The answer is unclear"
elif random_number == 12:
    answer = "Rotound and absolutely no"
elif random_number == 13:
    answer = "Oh, most definitely yes"
elif random_number == 14:
    answer = "Pfft, no? what did you expect, doofus"
elif random_number == 15:
    answer = "Hell no"
else:
     answer = "Error"

if question == "":
    print("You need to ask a question!")
else:
    if name == "":
        print("Question:", question)
    else:
        print(name, "asks:", question)
print("Magic 8-Baller's answer:", answer)
#CC1