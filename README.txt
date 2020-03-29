A program that makes personalised book recommendations using a similarity algorithm to predict
which books a user is likely to enjoy reading based on their past or sample ratings.

1. Describe any complex data structures you used and explain why you think they are suitable. 

I used a dictionary with string keys and list values for the ratings database because dictionaries have O(1) lookup. Furthermore,
I used a list for the similarities of users and their recommendations to be able to sort it (because lists are ordered).

2. How did you break down the problem into sub-problems? Explain the sub-problems and explain how they are organized in recommendations.py.

I started writing the program by thinking about the order of operations (e.g. a username cannot be checked against a databse if there is no database), so I started with
the reading of both necessary files (books.txt and ratings.txt). Then the username needs to be checked because there are two cases: either it is already in the database,
in which case nothing additional needs to be done, or it is a new user, in which case they need to rate 11 random books according to the rating rules. Once that is done,
the number of recommendations can be obtained and the similarity algorithm can be implemented. Finally, the recommendations themselves can be found with a sorted list of
users with high similarities and their sorted recommendations.


3. Are there any parts of your code that you think are difficult to understand? if yes, explain them here. 

The recommendations are given with the use of two "while" loops instead of "for" loops because the condition of the amount of recommendations given always needs to be held,
and the use of "break" is bad form. There are enough comments in the program that it should be understandable step-by-step.

4. Which possible errors could occur and how have you handled them? Explain whether you have used exception handling or defensive programming and use examples if you like.

I used exception handling for cases where a file could be non-existent (books.txt or ratings.txt) and defensive programming for wrong input by user for there not to be a
performance cost.