# Fortune Cookie Program 🥠
# This is so stupid. Literally stooooopid. Fortune cookies are so dumb. I hate them. I hate them so much. I hate them so much that I made a program that generates a random fortune for you. Just because.
# Enjoy! Sadly, I can't make it taste like a cookie. You'll have to do that yourself. 🍪
# Or not. Idk. You can buy some really good ones though. I recommend the ones with chocolate. They're really good. 🍫

import random

fortune = random.randint(0, 4)

if fortune == 0:
  print("May you one day be carbon neutral")
elif fortune == 1:  
  print("You have rice in your teeth")
elif fortune == 2:
  print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
  print("You're dumb")
elif fortune == 4:
  print("The fortune you seek is in another cookie")
#CC