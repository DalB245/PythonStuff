name = input("What's your Name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you in cm? "))

if age >= 18:
    print("Oh, you're a big Boy XD")
elif age <= 6:
    print("You're a small guy :)")
else:
    print("Hi :)")

print("Oh, hi " + str(name) + ". Nice to meet you :)")

print("Let's create your Username!")
random = input("Pick a random number! ")

username = name[0:3] + name[6] + str(age) + str(random[0:1])

print(username)
