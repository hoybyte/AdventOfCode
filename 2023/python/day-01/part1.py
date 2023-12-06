# Part 1 information goes below
import os
import re


def extract_digits(input_string):
    return [int(digit) for digit in re.findall(r'\d', input_string)]


def retrieve_first_last(input_string):
    


def calculate_total(input_string):
    return


try:
    # Get the script directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the relative path of the file

    file_path = os.path.join(script_directory, 'input.txt')

    # Print working directory
    current_directory = os.getcwd()
    print("Current Working Directory", current_directory)

    # Read strings from input.txt
    with open(file_path, 'r') as file:
        data = file.read().splitlines()

    result = [extract_digits(s) for s in data]

    print(result)

except FileNotFoundError:
    print("Error: The file 'input.txt' was not found in the current working directory. Please use the correct file path!")
except Exception as e:
    print(f"An unexpected error occured: {e}")

# Remove all characters except for Ints in String
# Number = f + s
# else f + f