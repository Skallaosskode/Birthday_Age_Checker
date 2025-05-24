name = input("What is your name? ").title()
age = int(input("What is your age? "))
genre = input("What is your favorite movie genre? ")
if genre == 'horror':
    print(f"""
    {name.title()} at {age} you're so brave!  Why not enjoy some
    chocolate eyeballs with your scary flick?
    """)
elif genre == 'comedy':
    print(f"""
    At {age}, laughing is the best medicine {name.title()}!  Why not enjoy
    some chocolate doo doo cookies with your comedy?
    """)
elif genre == 'romance':
    print(f"""
    I wonder if this one will be happily ever after, {name.title()}?
    Why not indulge in some triple dipped ice cream bites
    for this sweet lovey romance? {age} year olds love them!
    """)
elif genre == 'western':
    print(f"""
    Well giddyup {name.title()}! At {age} you must be great with a lasso!
    Why not lasso some beef jerky for the perfect pairing?
    """)
elif genre == 'sci-fi':
    print(f"""
    Get away from her you... nah just kidding {name.title()}!
    I really liked that one when i was {age} too.  Why not try the
    vanilla alien brains?
    """)
else:
    print(f"""
    A great choice {name.title()}. Good old popcorn with lots of
    butter is the obvious choice for this one.  So many {age} year olds
    say, its hard to beat!
    """)