import os
import shutil

folderToOrg = input("Enter the path of the folder to organize: ")
os.chdir(folderToOrg)  # this changes the current working directory to the specified input folder

print(f"What type of file do you want to organize?")
print("1. PDF files")
print("2. Image files")
print("3. Word files")
print("4. Excel files")
print("5. RAR files")
print("6. ZIP files")      # NEW
print("7. PPT files")      # NEW
choice = input("Enter your choice (1-7): ")

destination_path = input("Where do you want to move the files(path)? ")
os.chdir(destination_path)  # CHANGE to destination folder


current_folder = os.getcwd()
print(f"Current working directory: {current_folder}")
items = os.listdir(current_folder)
print(f"Items in the current working directory: {items} ")



def movePDF_To_One_Folder():
    os.makedirs("PDF", exist_ok=True)
    for item in items:
        item_path = os.path.join(current_folder, item)
        if os.path.isfile(item_path):
            name, ext = os.path.splitext(item)
            if ext.lower() == ".pdf":
                source_file = os.path.join(current_folder, item)
                destination_folder = os.path.join(current_folder, "PDF")
                destination_file = os.path.join(destination_folder, item)
                shutil.move(source_file, destination_file)
                print(f"Moved {item} to PDF folder")

def moveImage_TO_one_Folder():
    os.makedirs("Images", exist_ok=True)
    for item in items:
        item_path = os.path.join(current_folder, item)
        if os.path.isfile(item_path):
            name, ext = os.path.splitext(item)
            if ext.lower() in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
                source_file = os.path.join(current_folder, item)
                destination_folder = os.path.join(current_folder, "Images")
                destination_file = os.path.join(destination_folder, item)
                shutil.move(source_file, destination_file)
                print(f"Moved {item} to Images folder")

def moveWord_TO_one_Folder():
    os.makedirs("Word", exist_ok=True)
    for item in items:
        item_path = os.path.join(current_folder, item)
        if os.path.isfile(item_path):
            name, ext = os.path.splitext(item)
            if ext.lower() in [".docx", ".doc"]:
                source_file = os.path.join(current_folder, item)
                destination_folder = os.path.join(current_folder, "Word")
                destination_file = os.path.join(destination_folder, item)
                shutil.move(source_file, destination_file)
                print(f"Moved {item} to Word folder")

def moveExcel_TO_one_Folder():
    os.makedirs("Excel", exist_ok=True)
    for item in items:
        item_path = os.path.join(current_folder, item)
        if os.path.isfile(item_path):
            name, ext = os.path.splitext(item)
            if ext.lower() in [".xlsx", ".xls", ".csv"]:
                source_file = os.path.join(current_folder, item)
                destination_folder = os.path.join(current_folder, "Excel")
                destination_file = os.path.join(destination_folder, item)
                shutil.move(source_file, destination_file)
                print(f"Moved {item} to Excel folder")

def moveRar_TO_one_Folder():
    os.makedirs("Archives", exist_ok=True)
    for item in items:
        item_path = os.path.join(current_folder, item)
        if os.path.isfile(item_path):
            name, ext = os.path.splitext(item)
            if ext.lower() in [".rar", ".zip", ".7z"]:
                source_file = os.path.join(current_folder, item)
                destination_folder = os.path.join(current_folder, "Archives")
                destination_file = os.path.join(destination_folder, item)
                shutil.move(source_file, destination_file)
                print(f"Moved {item} to Archives folder")

# NEW FUNCTION FOR ZIP FILES
def moveZip_TO_one_Folder():
    os.makedirs("Zip_Files", exist_ok=True)
    for item in items:
        item_path = os.path.join(current_folder, item)
        if os.path.isfile(item_path):
            name, ext = os.path.splitext(item)
            if ext.lower() == ".zip":
                source_file = os.path.join(current_folder, item)
                destination_folder = os.path.join(current_folder, "Zip_Files")
                destination_file = os.path.join(destination_folder, item)
                shutil.move(source_file, destination_file)
                print(f"Moved {item} to Zip_Files folder")

# NEW FUNCTION FOR PPT FILES
def movePPT_TO_one_Folder():
    os.makedirs("PowerPoint", exist_ok=True)
    for item in items:
        item_path = os.path.join(current_folder, item)
        if os.path.isfile(item_path):
            name, ext = os.path.splitext(item)
            if ext.lower() in [".pptx", ".ppt"]:
                source_file = os.path.join(current_folder, item)
                destination_folder = os.path.join(current_folder, "PowerPoint")
                destination_file = os.path.join(destination_folder, item)
                shutil.move(source_file, destination_file)
                print(f"Moved {item} to PowerPoint folder")

# Run the selected function
if choice == "1":
    movePDF_To_One_Folder()
elif choice == "2":        
    moveImage_TO_one_Folder()
elif choice == "3":
    moveWord_TO_one_Folder()
elif choice == "4":
    moveExcel_TO_one_Folder()
elif choice == "5":
    moveRar_TO_one_Folder()
elif choice == "6":      # NEW
    moveZip_TO_one_Folder()
elif choice == "7":      # NEW
    movePPT_TO_one_Folder()
else:
    print("Invalid choice! Please enter 1-7")