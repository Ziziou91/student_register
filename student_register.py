"""Asks the user to input a number of students, then provide IDs for each before writing to reg_from.txt"""

def print_line(char="-", count=70) -> None:
    """Prints a line of characters for formatting in the terminal."""
    print(f"{char*count}")

def bold_text(text: str) -> str:
  """Returns a bolded string for printing."""
  return "\033[1m" + text + "\033[0m"

def get_int_input() -> str:
    """Takes a user input, ensure it can cast as an integer and then returns."""
    student_count_str = input("Enter an integer: ")
    try:
        student_count_int = int(student_count_str)
    except ValueError:
        print(f"{"="*10}Error! {student_count_str} is not a valid integer. Please try again.{"="*10}")
        return get_int_input()
    else: 
        return student_count_int

def write_string_to_file(file_name: str, user_string: str) -> None:
    """Checks a given file_name is valid before writing user_string to it."""
    try:
        file = open(file_name, "w", encoding="UTF-8")
    except FileNotFoundError:
        print(f"error, {file_name} is an invalid path.")
    else:
        with file:
            file.write(user_string)
    
def app() -> None:
    """Runs the logic for student_register"""
    file = "reg_form.txt"
    register= ""
    print(f"{bold_text('\nHow many students are you registering for the exam venue?\n')}")
    my_int = get_int_input()
    for n in range(my_int):
        register += f"{input("Enter a student ID number: ")} {'_'*20}\n"
    write_string_to_file(file, register)

print_line(char="=")
print(f"{'*'*25}{bold_text('student_register.py')}{'*'*26}")
print_line(char="=")

app()

print_line(char="=")
print(f"{'*'*24}{bold_text('student_register.py END')}{'*'*23}")
print_line(char="=")
