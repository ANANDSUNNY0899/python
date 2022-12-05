temp_var = ""
i = 0 
name = input =("enter your name ")
while i < len(name):
    if name[i] not in temp_var:
    print(f"{name[i]} : {name.count(name[i])}")
    
