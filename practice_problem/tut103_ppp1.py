# Age Problem !
# we have to detect - user have input age or year of birth.
# --> tell them when they will turn 100 years.
#  --> they will provide a year and we have to tell what will be their age at that year.

current_year = 2025
time = int(input("Enter your age or year of birth: "))
if(time <124 and time >0):
    age = time
    year_of_birth = 2025 - age
    # in which year you will turn 100 years - logic
    # year of birth -> 2025-age
    print(f"You will turn 100 years of age at the year: {2025-age + 100}")

elif(time>1900 and time<2026):
    year_of_birth = time
    age = 2025 - year_of_birth
    print(f"You will turn 100 years of age at year: {year_of_birth+100}")

if(age > 123):
    print("You are the greatest alive person")
elif(year_of_birth > 2025):
    print("You are not yet born")

choice = input("You want to know your age in a entered year: y or n \n")
if(choice == 'y'):
    year = int(input("Enter the year: "))
    if(len(str(time)) < 4 and len(str(time)) > 0):   # user have input the age
        if(year < (2025-age)):    # error handling
            raise ValueError("Year entered  is before your time of birth")
        else:
            print(f"You will be {year - (2025-time)} year old")
    if(len(str(time)) == 4):
        if(year < time):    # error handling
            raise ValueError("Year entered  is before your time of birth")
        else:
            print(f"You will be {year - time} year old")

elif(choice == 'n'):
    print("Make yourself great.")

else:
    print("Invalid Choice.")
