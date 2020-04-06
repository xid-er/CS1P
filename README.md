# Book Recommendations Program

## Description
A program that makes personalised book recommendations using a similarity algorithm to predict
which books a user is likely to enjoy reading based on their past or sample ratings.

## Complex data structures
I used a dictionary with string keys and list values for the ratings database because dictionaries have O(1) lookup. Furthermore,
I used a list for the similarities of users and their recommendations to be able to sort it (because lists are ordered).

## Sub-problems
I started writing the program by thinking about the order of operations (e.g. a username cannot be checked against a databse if there is no database), so I started with
the reading of both necessary files (books.txt and ratings.txt). Then the username needs to be checked because there are two cases: either it is already in the database,
in which case nothing additional needs to be done, or it is a new user, in which case they need to rate 11 random books according to the rating rules. Once that is done,
the number of recommendations can be obtained and the similarity algorithm can be implemented. Finally, the recommendations themselves can be found with a sorted list of users with high similarities and their sorted recommendations.

## Excuses and Explanations
The recommendations are given with the use of two "while" loops instead of "for" loops because the condition of the amount of recommendations given always needs to be held,
and the use of "break" is bad form. There are enough comments in the program that it should be understandable step-by-step.

## Error handling
I used exception handling for cases where a file could be non-existent (books.txt or ratings.txt) and defensive programming for wrong input by user for there not to be a
performance cost.
