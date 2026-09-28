name = input("Enter your name: ")
age = input("Enter your age: ")
favNum = input("Enter your favorite number: ")

age = int(age)
favNum = int(favNum)

ageIn10 = age + 10
print("Age in ten years is", ageIn10)

squaredFavNum = favNum ** 2
print("The square of favorite number is", squaredFavNum)

if favNum % 2 == 0:
    status = "even"
else:
    status = "odd"
 
print("Your favorite number is", status)

print(f"Hi {name}! In 10 years you'll be {ageIn10}. Your favorite number squared is {squaredFavNum}, and it's {status}")


"""
Python treats everything we input as a raw text to ensure it never guesses type of variable wrong or changes what you typed.
"""