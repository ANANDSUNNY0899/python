name ,char = input("enter comma seperated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name. strip().lower().count(char.strip().lower())}")