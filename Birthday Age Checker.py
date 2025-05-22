name = input("What is your name? ")
birth_year = int(input("What is your birth year? "))
age = 2025 - birth_year
if age <= 12:
    print(f"Hello, {name} you're {age} years old and are a child!  Please enjoy a Spongebob Squarepants hat!")
elif 13 <= age <= 18:
    print(f"Hello, {name} you're {age} years old and are a teen!  Please enjoy an Amoung Us tee shirt!")
else:
    print(f"Hello, {name} you're {age} years old and are an adult!  Please enjoy these Rick & Morty socks!")