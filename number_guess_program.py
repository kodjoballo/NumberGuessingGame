import random

user_level = ""
user_number = int(0)
trial_count = int(0)
random_integer = int(0)

random_integer = random.randint(1,100)
#print(f"Random integer between 0 and 100: {random_integer}")
print("\n")
print("----------------------------")
print("-----Game guess a number----")
print("----------------------------")
print("\n")


user_level = input("Choose Level E (Easy), N (Normal), D (Difficult): " ).upper()

while user_level.upper() != 'E' and user_level.upper() != 'N' and user_level.upper() != 'D':
    print("wrong choice!!!")
    user_level = input("Kindly make another choice: ")

if user_level == "E":
    print("You have 15 trials time to find the number !!!")
    while True and trial_count < 15:
        user_number =int (input("What is the number: "))
        if user_number < random_integer:
            print("Guess greater than that!")
            trial_count += 1
        elif user_number > random_integer:
            print("Guess less than that! ")
            trial_count += 1

        else:
            trial_count += 1
            print("\n")
            print("*************************************************************************************")
            print(f"Congratulations!!!!, you have found the number in {trial_count} guesses in easy mode")
            print("*************************************************************************************")

            break

    if trial_count == 15:
        print("\n")
        print("OH OOOOH You have lost by exceeding the number of 15 trials ")

elif user_level == "N":

    print("You have 12 trials time to find the number !!!")
    while True and trial_count < 12:
        user_number = int(input("What is the number: "))
        if user_number < random_integer:
            print("Guess greater than that!")
            trial_count += 1
        elif user_number > random_integer:
            print("Guess less than that! ")
            trial_count += 1

        else:
            trial_count += 1
            print("\n")
            print("****************************************************************************************")
            print(f"Congratulations!!!!, you have found the number in {trial_count} guesses in normal mode")
            print("*****************************************************************************************")

            break

    if trial_count == 12:
        print("\n")
        print("OH OOOOH You have lost by exceeding the number of 12 trials ")

else:
    print("You have 8 trials time to find the number !!!")
    while True and trial_count < 8:
        user_number = int(input("What is the number: "))
        if user_number < random_integer:
            print("Guess greater than that!")
            trial_count += 1
        elif user_number > random_integer:
            print("Guess less than that! ")
            trial_count += 1

        else:
            trial_count += 1
            print("\n")
            print("*******************************************************************************************")
            print(f"Congratulations!!!!, you have found the number in {trial_count} guesses in difficult mode")
            print("*******************************************************************************************")

            break

    if trial_count == 8:
        print("\n")

        print("OH OOOOH You have lost by exceeding the number of 8 trials ")



