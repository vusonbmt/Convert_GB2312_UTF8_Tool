# Convert_GB2312_UTF8_Tool

Since some code archived in GB2312 in Chinese Simplified environments was garbled in other environments which can read on Notepad++ but break font when open in VS Code and some time could not be built by Visual Studio
I wrote a small program that converted all files in folder to UTF-8.

This code will convert all .c and .h files to UTF-8 encoding and save them with the same name.
You can run this code by passing the folder path as a command-line argument when you run the script, like this:
```
python convert2utf8.py /path/to/folder
```

Sample for windows user:
```
python convert2utf8.py C:\Users\username\Documents\folder
```
