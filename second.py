# Blood-donation
age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))

if age >= 18 and age <= 60 and weight >= 50:
    print("You can donate blood")

else:
    print("You can't donate blood")