# Function with outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didnt provide valid inputs." #for termination of function
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result:{formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"),
input("what is your last name?")))


