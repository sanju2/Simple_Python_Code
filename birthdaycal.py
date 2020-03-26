# Simple Age Converter
UserInput = input(
    "Simple Age Converter(Sanju) \n Enter Your Birth Day(year) : ")
print("Your Birth Year : " + UserInput)
BD = 2020 - int(UserInput)
Agev1 = "Oyage Wayasa : "
Age = f"{Agev1} {BD}"
print(BD)

# If Condition
if int(BD) < 20:
    print("You are a Student")

elif 18 < int(BD) <= 25:
    print("You are a Teenager")

else:
    print("You are a Elder")
