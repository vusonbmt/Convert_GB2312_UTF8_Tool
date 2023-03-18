# -*- coding: utf-8 -*-
import sys
import os
import glob
import codecs

# This code will convert all .c and .h files to UTF-8 encoding and save them with the same name.
def get_files_by_extension(folder_path, extension):
    file_pattern = os.path.join(folder_path, '**', f'*{extension}')
    return glob.glob(file_pattern, recursive=True)

def convert_encoding(file_path, input_encoding, output_encoding):
    with codecs.open(file_path, 'r', encoding=input_encoding) as file:
        content = file.read()
    with codecs.open(file_path, 'w', encoding=output_encoding) as file:
        file.write(content)

def is_valid_encoding(file_path, output_encoding):
    try:
        with codecs.open(file_path, 'r', encoding=output_encoding) as file:
            file.read()
        return True
    except UnicodeDecodeError:
        print(f"Error: {file_path} contains illegal multibyte sequence.")
        return False
    
def convert_files_encoding(folder_path, extensions, input_encoding, output_encoding):
    files = []
    for extension in extensions:
        files += get_files_by_extension(folder_path, extension)

    for file in files:
        try:
            # Get the directory and name of the file
            file_dir, file_name = os.path.split(file)
            # Set the full path of the new file with the same extension
            new_file_path = os.path.join(file_dir, file_name)
            # Check if the file can be encoded with the output encoding 
            if is_valid_encoding(file, output_encoding):
                # Convert the encoding of the file and save it with the same name
                convert_encoding(file, input_encoding, output_encoding)
                os.rename(file, new_file_path)
            else:
                print(f"Skipping file: {file}")            
        except Exception as e:
            print(f"Error converting {file}: {e}")            
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python file_search.py folder_path")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print('Error: folder_path is not a valid directory.')
        sys.exit(1)

    input_encoding = 'gb2312'
    output_encoding = 'utf-8'
    extensions = ['.c', '.h']

    for extension in extensions:
        files = get_files_by_extension(folder_path, extension)
        print(f"Files with extension '{extension}':")
        print(files)

    convert_files_encoding(folder_path, extensions, input_encoding, output_encoding)
    print('Files converted to UTF-8 encoding and saved with the same name.')


if __name__ == "__main__":
    main()
