# Practicing

def render_fnc(para):
    print(f"{para} is logged in")


Name = "Samuel"
Pwd = "123@"
valid = False
name = input("Enter your name: ")
password = input("Ender your password: ")
# if Pwd == password:
#     valid = True
valid = Pwd == password
valid and render_fnc(name)
not valid and render_fnc("ERROR: Nobody")
list_1 = [1, 2, 3, "4", "5", 12]
dict_ = {name: "Samuel", "age": 29}
tuple_ = ("1", "2", "3")









