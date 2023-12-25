# Get the age and citizenship status from the user
age = int(input("Enter your age: "))
is_citizen = input("Are you a citizen? (yes/no): ").lower()

# Check eligibility for voting
if age >= 18:
    if is_citizen == "yes":
        print("You are eligible to vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are not eligible to vote because you are under 18 years old.")