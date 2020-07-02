# Book recommendation program by Kārlis Siders, 2467273S, CS1S, LB01




import random

# Reading books.txt

books = []
try:
    with open('books.txt', 'r') as b:
        for i in b.readlines():
            data = i.strip().split(',')
            books.append([data[0],data[1]])
except:
    with open('output.txt','w') as o:
            o.write("404: books.txt not found.")
else:
    
    # Reading ratings.txt

    try:
        ratings = {}
        with open('ratings.txt','r') as r:
            ratings_text = r.readlines()
            for i in range(0, len(ratings_text), 2):
                name = ratings_text[i].strip()
                numbers_chars = ratings_text[i+1].strip().split()
                numbers = [int(x) for x in numbers_chars]
                ratings[name] = numbers
    except:
        with open('output.txt','w') as o:
            o.write("404: ratings.txt not found.")
    else:

        # Username

        user_completed = False
        while not user_completed:
            print("What is your name? ", end='')
            user = input()
            if user not in ratings:
                print("Are you sure you want to create a new profile? y/n")
                new_user = input()
                if new_user == 'y':
                    user_completed = True
            else:
                new_user = False
                user_completed = True

        # New user ratings

        if new_user == 'y':

            # New rating
            
            new_ratings = ([0] * len(books)).copy()
            rand_books = random.sample(list(range(len(books))), 11)
            print("What did you think of these books?")
            print("-5: Hated it!")
            print("-3: Didn't like it")
            print("0: Haven't read it")
            print("1: It was OK")
            print("3: Liked it!")
            print("5: Loved it!")
            for i in rand_books:
                author = books[i][0]
                title = books[i][1]
                rated = False
                while not rated:
                    print("What did you think of {title} by {author}?".format(title=title,author=author))
                    temp = input()
                    try:
                        rating = int(temp)
                        if( rating == -5 or rating == -3 or rating == 0
                        or rating == 1 or rating == 3 or rating == 5):
                            rated = True
                            new_ratings[i] = rating
                        else:
                            print("Please enter one of the possible ratings")
                    except ValueError:
                        print("Please enter a valid number")
            ratings[user] = new_ratings

            # Updating ratings.txt
            with open('ratings.txt', 'a') as h:
                h.write(user+'\n')
                h.write(' '.join([str(r) for r in new_ratings])+'\n')

        # Number of recommendations

        recs_completed = False
        while not recs_completed:
            print("How many recommendations? ", end='')
            temp = input()
            if temp.isnumeric():
                recs_needed = int(temp)
                if recs_needed > 0:
                    recs_completed = True
                elif recs_needed == 0:
                    print("What's the point then?")
                    recs_completed = True
                else:
                    print("Please enter a valid positive number")
            else:
                print("Please enter a valid positive number")


        # Similarity algorithm

        def similarity(user, other):
            sum = 0
            for i in range(len(books)):
                sum += ratings[user][i] * ratings[other][i]
            return sum

        # Finding similarities

        similarities = []
        for i in ratings:
            if user != i:
                similarities.append([i,similarity(user, i)])

        similarities.sort(key = lambda x: x[1], reverse = True)

        # FINDING THE RECOMMENDATIONS

        with open('output.txt','w') as o:

            o.write("What is your name? {name}\n".format(name=user))
            o.write("How many recommendations? {recs}\n\n".format(recs=recs_needed))
            recs_given = 0
            i = 0
            n = len(similarities)
            recs_given_titles = []

            # Going through all users

            while i < n and recs_given < recs_needed:
                j = 0
                m = len(books)
                similar = similarities[i][0]
                similarity = similarities[i][1]

                recs_given_list = []

                # Going through all ratings by user
                
                while j < m and recs_given < recs_needed and similarity > 20:
                    author = books[j][0]
                    title = books[j][1]
                    rating = ratings[similar][j]
                    if( (rating == 3 or rating == 5)
                        and ratings[user][j] == 0
                        and title not in recs_given_titles):
                            
                            recs_given += 1
                            recs_given_titles.append(title)
                            recs_given_list.append([rating,title,author])
                    j += 1

                # To output file
                
                if len(recs_given_list) != 0:
                    o.write("{similar} recommends:\n".format(similar=similar))
                    print("{similar} recommends:".format(similar=similar))
                    recs_given_list.sort(key = lambda x: x[0], reverse = True)
                    for k in recs_given_list:
                        rating = k[0]
                        title = k[1]
                        author = k[2]
                        o.write("    {title} by {author} ({rating})\n".format(title=title, author=author, rating=rating))
                        print("    {title} by {author} ({rating})".format(title=title, author=author, rating=rating))
                i += 1
            if recs_given == 0:
                o.write("\nSorry, you have read too few books.")
            elif recs_given < recs_needed:
                o.write("\nSorry, our database is still growing, so we could only offer you {recs} recommendations.".format(recs=recs_given))
            wait_for_end = input()
