def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif 5 < rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"

print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."