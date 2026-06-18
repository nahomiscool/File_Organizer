# 📁 Python File Organizer

A simple yet powerful Python script that automatically organizes files in your folders based on their type. Perfect for cleaning up your Downloads folder or organizing project files!

## ✨ Features

- 🗂️ **Organize files by type** - PDF, Images, Word, Excel, Archives, ZIP, PowerPoint, and more
- 📍 **Custom destination** - Choose where to move your organized files
- 🔄 **Safe moving** - Handles duplicate filenames automatically (adds numbers to avoid overwriting)
- 🎯 **Selective organization** - Choose exactly which file type to organize
- 📊 **Progress tracking** - See which files are being moved in real-time

## 🚀 Supported File Types

| Option | File Type | Extensions |
|--------|-----------|------------|
| 1 | PDF Files | `.pdf` |
| 2 | Image Files | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| 3 | Word Files | `.docx`, `.doc` |
| 4 | Excel Files | `.xlsx`, `.xls`, `.csv` |
| 5 | Archives (RAR) | `.rar`, `.zip`, `.7z` |
| 6 | ZIP Files | `.zip` |
| 7 | PowerPoint | `.pptx`, `.ppt` |

## 📋 Prerequisites

- Python 3.6 or higher
- No additional libraries required! (Uses only built-in modules: `os` and `shutil`)

## 💻 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-file-organizer.git

# Navigate to the project directory
cd python-file-organizer

🎮 Usage
Run the script:
bash

python file_organizer.py

Step-by-step:

    Enter the folder path - The folder containing files you want to organize

    Choose file type - Select a number from the menu (1-7)

    Enter destination path - Where you want the organized files to be moved

Example:
text

Enter the path of the folder to organize: C:\Users\John\Downloads
What type of file do you want to organize?
1. PDF files
2. Image files
3. Word files
4. Excel files
5. RAR files
6. ZIP files
7. PPT files
Enter your choice (1-7): 1
Where do you want to move the files(path)? C:\Users\John\Documents\PDFs

Output:
Current working directory: C:\Users\John\Documents\PDFs
Items in the current working directory: ['report.pdf', 'invoice.pdf', 'photo.jpg']
Moved report.pdf to PDF folder
Moved invoice.pdf to PDF folder

🗂️ How It Works

    The script changes to the source folder you specified

    Scans all files in that folder

    Checks each file's extension against your chosen category

    Creates the destination folder if it doesn't exist

    Moves matching files to the destination folder

    Prints progress for each file moved

🔧 Customization
Adding New File Types

To add support for new file types, follow this pattern:
python

def moveMUSIC_TO_one_Folder():
    current_folder = os.getcwd()
    items = os.listdir(current_folder)
    os.makedirs("Music", exist_ok=True)
    for item in items:
        item_path = os.path.join(current_folder, item)
        if os.path.isfile(item_path):
            name, ext = os.path.splitext(item)
            if ext.lower() in [".mp3", ".wav", ".flac", ".aac"]:
                source_file = os.path.join(current_folder, item)
                destination_folder = os.path.join(current_folder, "Music")
                destination_file = os.path.join(destination_folder, item)
                shutil.move(source_file, destination_file)
                print(f"Moved {item} to Music folder")

Then add it to the menu:
python

print("8. Music files")
# And in the if/elif chain:
elif choice == "8":
    moveMUSIC_TO_one_Folder()

⚠️ Important Notes

    No Undo Feature - This script permanently moves files. Consider backing up important files before running.

    No Duplicate Overwriting - If a file with the same name exists, the script adds a number (e.g., file_1.pdf)

    Windows/Mac/Linux - Works on all operating systems with Python

🐛 Troubleshooting
Common Issues:
Problem	Solution
"FileNotFoundError"	Check if the folder path exists and is spelled correctly
"Permission denied"	Close the file in any program (Word, Photoshop, etc.) before running
Files not moving	Make sure you're choosing the correct option and files have matching extensions
"Invalid choice"	Enter a number between 1 and 7 only
🚀 Future Improvements

    Add option to organize ALL file types at once

    Add undo functionality

    Add progress bar for large folders

    Add configuration file for custom categories

    Add GUI version using Tkinter

    Add scheduling option (automatically run daily)

📄 License

This project is open source and available under the MIT License.
🤝 Contributing

Contributions are welcome! Feel free to:

    Fork this repository

    Add new file types

    Improve the code

    Submit a pull request

📧 Contact

Have questions or suggestions? Open an issue on GitHub!
