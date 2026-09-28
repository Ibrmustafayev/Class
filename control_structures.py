grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Your grade is A")
elif grade >= 75:
    print("Your grade is B")
elif grade >= 50:
    print("Your grade is C")
else:
    print("Your grade is F")

#----------------------------------------

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(i, "*", number, "=", i * number)

#----------------------------------------

password = "abc123"
i = 3

while i > 0:
    enteredPass = input("Enter password: ")

    if password == enteredPass:
        print("Welcome!!!")
        break

    print("Wrong password!")

    if i == 1:
        print("Attempts ended!")
    i -= 1