email = "vinod.kumar@gmail.com"
at_index = email.find("@")
print("@ index:", at_index)

dot_index = email.find(".", at_index + 1)
print(". index:", dot_index)

u_index = email.find("_")
print("_ index:", u_index)

if at_index == -1 or dot_index == -1:
    print("Invalid email address:", email)
