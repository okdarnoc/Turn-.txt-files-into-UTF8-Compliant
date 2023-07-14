import os
import string

def remove_non_utf8_compliant_characters(text):
    # Create a set of all printable characters.
    printable = set(string.printable)
    # Remove the vertical tab character since it's not UTF-8 compliant.
    printable.remove("\x0b")
    # Only retain characters that are present in the 'printable' set.
    return ''.join(filter(lambda x: x in printable, text))

def convert_files_in_directory(directory):
    # Walk through every file in the specified directory.
    for filename in os.listdir(directory):
        # If the file is a text file, we want to process it.
        if filename.endswith('.txt'):
            # Construct the full path of the file.
            file_path = os.path.join(directory, filename)
            # Open the file with the 'ignore' error handling mode to avoid issues with non-utf8 characters.
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                # Read the file's content.
                content = f.read()
            # Remove non-UTF8 compliant characters from the content.
            cleaned_content = remove_non_utf8_compliant_characters(content)
            # Open the file again, this time in write mode.
            with open(file_path, 'w', encoding='utf-8') as f:
                # Write the cleaned content back into the file.
                f.write(cleaned_content)

if __name__ == '__main__':
    # Ask the user to enter the directory path they want to process.
    directory = input("Enter the directory path: ")
    # Call the function to start the cleaning process.
    convert_files_in_directory(directory)
