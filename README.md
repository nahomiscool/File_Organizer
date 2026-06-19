# 📁 Python File Organizer

A powerful file organization tool with **both Terminal and GUI interfaces**! Automatically sort your files into organized folders based on file type. Perfect for cleaning up your Downloads folder, organizing project files, or maintaining a tidy workspace.

## ✨ Features

### Both Versions:
- 🗂️ **Organize files by type** - PDF, Images, Word, Excel, Archives, ZIP, PowerPoint, and more
- 📍 **Custom destination** - Choose where to move your organized files
- 🔄 **Safe moving** - Handles duplicate filenames automatically (adds numbers to avoid overwriting)
- 🎯 **Selective organization** - Choose exactly which file type to organize
- 📊 **Progress tracking** - See which files are being moved in real-time

### GUI Version Only:
- 🖥️ **User-friendly interface** - No command line needed!
- 📂 **Browse buttons** - Easily select folders with a visual browser
- 📊 **Progress bar** - Visual progress indicator
- 💬 **Status updates** - Real-time feedback on file operations
- 🎨 **Clean design** - Professional and intuitive layout

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
- **Terminal Version**: No additional libraries required (uses only built-in modules: `os` and `shutil`)
- **GUI Version**: Uses built-in `tkinter` (usually comes with Python on Windows/Mac, may need installation on Linux)

### Installing tkinter on Linux:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

💻 Installation
```bash

# Clone the repository
git clone https://github.com/yourusername/python-file-organizer.git

# Navigate to the project directory
cd python-file-organizer
```
🎮 Usage
Option 1: Terminal Version
```bash

python file_organizer_terminal.py
```
Step-by-step:

    Enter the folder path containing files to organize

    Choose a file type from the menu (1-7)

    Enter the destination path where you want files moved

Example Output:
```text

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

Moved report.pdf to PDF folder
Moved invoice.pdf to PDF folder
✅ Successfully moved 2 files!
```
Option 2: GUI Version (Recommended for Beginners)
```bash

python file_organizer_gui.py
```
Step-by-step:

    Click Browse to select your Source Folder (where files are currently located)

    Click Browse to select your Destination Folder (where you want files moved)

    Select the file type you want to organize using the radio buttons

    Click ORGANIZE FILES

    Watch the progress bar and status updates!

GUI Preview:
```text

+------------------------------------------+
|         📁 File Organizer                 |
|                                           |
|  Source Folder:    [C:\Users\John\DL] [Browse] |
|  Destination Folder:[C:\Users\John\Docs] [Browse] |
|  ───────────────────────────────────────   |
|  Select File Type to Organize:            |
|  ○ 1. PDF Files                          |
|  ○ 2. Image Files                        |
|  ○ 3. Word Files                         |
|  ○ 4. Excel Files                        |
|  ○ 5. RAR/Archive Files                  |
|  ○ 6. ZIP Files                          |
|  ○ 7. PowerPoint Files                    |
|                                           |
|         [ ORGANIZE FILES ]                |
|                                           |
|  Status: Ready                            |
|  [████████████░░░░░░░░░] 75%              |
+------------------------------------------+
```
📁 Project Structure
```text

python-file-organizer/
├── file_organizer_terminal.py   # Terminal/Command Line version
├── file_organizer_gui.py        # GUI version with tkinter
├── README.md                    # This file
├── LICENSE                      # MIT License
└── .gitignore                   # Git ignore file
```
🔧 Customization
Adding New File Types
In Terminal Version:
```python

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

# Add to menu:
print("8. Music files")
# Add to if/elif chain:
elif choice == "8":
    moveMUSIC_TO_one_Folder()
```
In GUI Version:

Add to the radio button options in setup_ui():
```python

radio_options = [
    # ... existing options ...
    ("8. Music Files", 8)
]
```
Then add to the dictionaries in organize_files():
```python

file_types = {
    # ... existing types ...
    8: (".mp3", ".wav", ".flac", ".aac")
}

folder_names = {
    # ... existing names ...
    8: "Music"
}
```
🎯 Which Version Should I Use?
Version	Best For
Terminal	Advanced users, scripting, automation, remote servers
GUI	Beginners, visual users, occasional organization
⚠️ Important Notes

    No Undo Feature - Files are permanently moved. Consider backing up important files before running.

    No Duplicate Overwriting - If a file with the same name exists, the script adds a number (e.g., file_1.pdf)

    Cross-Platform - Works on Windows, Mac, and Linux

    GUI Requires tkinter - Usually installed with Python, but may need separate installation on Linux

🐛 Troubleshooting
Common Issues:
Problem	Solution
"No module named tkinter"	Install tkinter using your package manager (see Prerequisites)
"Permission denied"	Close the file in any program before running
Files not moving	Make sure you're choosing the correct option and files have matching extensions
"FileNotFoundError"	Check that the folder path exists and is spelled correctly
GUI won't open	Try running the terminal version to see if Python is working correctly
🚀 Future Improvements

    Add option to organize ALL file types at once

    Add undo functionality

    Add "Move" vs "Copy" option

    Add configuration file for custom categories

    Add dark mode for GUI

    Add folder preview in GUI

    Add scheduling option (automatically run daily)

    Add drag-and-drop support for GUI

📄 License

This project is open source and available under the MIT License.
🤝 Contributing

Contributions are welcome! Feel free to:

    Fork this repository

    Add new file types

    Improve the code

    Submit a pull request

    Report bugs via Issues

📝 Changelog
v2.0.0

    Added GUI version with tkinter interface

    Added progress bar and status updates

    Added visual folder selection with Browse buttons

v1.0.0

    Initial terminal version

    Support for 7 file types

    Duplicate file handling

Made with ❤️ using Python
⭐ Star this repository if you found it useful!


