"""Asks the user to input a number of students, then provide IDs for each before writing to reg_from.txt"""

def print_line(char="-", count=70) -> None:
    print(f"{char*count}")

def bold_text(text) -> str:
  return "\033[1m" + text + "\033[0m"

def get_input() -> str:
    """Takes a user input, ensure it can cast as an integer and then returns."""
    student_count_str = input("Enter an integer: ")
    try:
        student_count_int = int(student_count_str)
    except ValueError:
        print(f"{"="*10}Error! {student_count_str} is not a valid integer. Please try again.{"="*10}")
        return get_input()
    else: 
        return student_count_int

def app() -> None:
    file = "reg_form.txt"
    register= ""
    print(f"{bold_text('\nHow many students are you registering for the exam venue?\n')}")
    my_string = get_input()

    print(my_string)
   
print_line(char="=")
print(f"{'*'*25}{bold_text('student_register.py')}{'*'*26}")
print_line(char="=")


app()

print_line(char="=")
print(f"{'*'*24}{bold_text('student_register.py END')}{'*'*24}")
print_line(char="=")
