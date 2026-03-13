birthdays = {}

#Taking input for 5 birthdays
for i in range(5):
    name= input("Enter friend's name:")
    birthday= input("Enter their birthday (DD/MM): ")
    birthdays[name]= birthday

print("\nStored Birthdays")
for name in birthdays:
 print(name, ":", birthdays[name])