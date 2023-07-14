UTF-8 Compliant Text Files Cleaner
This Python script helps to clean up text files in a specified directory by removing non-UTF8 compliant characters.

##Getting Started
Prerequisites
Make sure you have the following installed on your system:

Python 3.6 or above
Usage
This script is designed to be run from the command line. It will prompt you to enter the path to the directory containing the text files you want to clean.

Example:

bash
Copy code
python3 utf8_text_cleaner.py
Enter the directory path: /path/to/your/directory
Code Overview
The script consists of two main functions:

remove_non_utf8_compliant_characters(text): This function removes non-UTF8 compliant characters from the provided text.

convert_files_in_directory(directory): This function walks through every file in the specified directory. If the file is a text file, it will read the content, clean it by removing non-UTF8 compliant characters, and then write the cleaned content back into the file.

Here is the main structure of the script:

python
Copy code
import os
import string

def remove_non_utf8_compliant_characters(text):
    ...
    return ''.join(filter(lambda x: x in printable, text))

def convert_files_in_directory(directory):
    ...
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            ...
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)

if __name__ == '__main__':
    directory = input("Enter the directory path: ")
    convert_files_in_directory(directory)
For the complete code and further details, refer to the script file.

License
This project is licensed under the terms of the MIT license.
