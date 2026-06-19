import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Variables
        self.source_folder = tk.StringVar()
        self.destination_folder = tk.StringVar()
        self.choice = tk.IntVar()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="File Organizer", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)
        
        # Source Folder Selection
        frame1 = tk.Frame(self.root)
        frame1.pack(pady=10, padx=20, fill="x")
        
        tk.Label(frame1, text="Source Folder:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
        tk.Entry(frame1, textvariable=self.source_folder, width=40).grid(row=0, column=1, padx=5)
        tk.Button(frame1, text="Browse", command=self.browse_source, bg="#494949", fg="white").grid(row=0, column=2)
        
        # Destination Folder Selection
        frame2 = tk.Frame(self.root)
        frame2.pack(pady=10, padx=20, fill="x")
        
        tk.Label(frame2, text="Destination Folder:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
        tk.Entry(frame2, textvariable=self.destination_folder, width=40).grid(row=0, column=1, padx=5)
        tk.Button(frame2, text="Browse", command=self.browse_destination, bg="#494949", fg="white").grid(row=0, column=2)
        
        # Separator
        ttk.Separator(self.root, orient='horizontal').pack(fill='x', pady=10)
        
        # File Type Selection
        tk.Label(self.root, text="Select File Type to Organize:", font=("Arial", 12, "bold")).pack(pady=5)
        
        # Radio buttons for file types
        frame3 = tk.Frame(self.root)
        frame3.pack(pady=5)
        
        radio_options = [
            ("1. PDF Files", 1),
            ("2. Image Files", 2),
            ("3. Word Files", 3),
            ("4. Excel Files", 4),
            ("5. RAR/Archive Files", 5),
            ("6. ZIP Files", 6),
            ("7. PowerPoint Files", 7)
        ]
        
        for text, value in radio_options:
            tk.Radiobutton(frame3, text=text, variable=self.choice, value=value, 
                          font=("Arial", 10)).pack(anchor="w", padx=20)
        
        # Organize Button
        organize_btn = tk.Button(self.root, text="ORGANIZE FILES", 
                                 command=self.organize_files,
                                 bg="#462F1A", fg="white", 
                                 font=("Arial", 14, "bold"),
                                 height=2, width=30)
        organize_btn.pack(pady=20)
        
        # Status Label
        self.status_label = tk.Label(self.root, text="Ready", font=("Arial", 10), fg="blue")
        self.status_label.pack(pady=5)
        
        # Progress Bar
        self.progress = ttk.Progressbar(self.root, length=400, mode='determinate')
        self.progress.pack(pady=10)
        
    def browse_source(self):
        folder = filedialog.askdirectory(title="Select Source Folder")
        if folder:
            self.source_folder.set(folder)
            
    def browse_destination(self):
        folder = filedialog.askdirectory(title="Select Destination Folder")
        if folder:
            self.destination_folder.set(folder)
    
    def move_files(self, source_folder, dest_folder, extensions, folder_name):
        try:
            # Create destination folder if it doesn't exist
            dest_path = os.path.join(dest_folder, folder_name)
            os.makedirs(dest_path, exist_ok=True)
            
            # Get all items in source folder
            items = os.listdir(source_folder)
            moved_count = 0
            total_files = len([item for item in items if os.path.isfile(os.path.join(source_folder, item))])
            
            if total_files == 0:
                messagebox.showinfo("Info", "No files found in source folder!")
                return 0
            
            for i, item in enumerate(items):
                item_path = os.path.join(source_folder, item)
                if os.path.isfile(item_path):
                    name, ext = os.path.splitext(item)
                    if ext.lower() in extensions:
                        source_file = os.path.join(source_folder, item)
                        destination_file = os.path.join(dest_path, item)
                        shutil.move(source_file, destination_file)
                        moved_count += 1
                        # Update progress
                        self.progress['value'] = (i + 1) / total_files * 100
                        self.root.update_idletasks()
            
            return moved_count
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return 0
    
    def organize_files(self):
        # Validate inputs
        source = self.source_folder.get()
        dest = self.destination_folder.get()
        choice = self.choice.get()
        
        if not source:
            messagebox.showerror("Error", "Please select a source folder!")
            return
            
        if not dest:
            messagebox.showerror("Error", "Please select a destination folder!")
            return
            
        if choice == 0:
            messagebox.showerror("Error", "Please select a file type!")
            return
            
        # Reset progress
        self.progress['value'] = 0
        self.status_label.config(text="Organizing files...", fg="orange")
        self.root.update_idletasks()
        
        # Define file extensions and folder names
        file_types = {
            1: (".pdf", "PDF"),
            2: (".jpg", ".jpeg", ".png", ".gif", ".bmp"),
            3: (".docx", ".doc"),
            4: (".xlsx", ".xls", ".csv"),
            5: (".rar", ".zip", ".7z"),
            6: (".zip", "Zip_Files"),
            7: (".pptx", ".ppt")
        }
        
        folder_names = {
            1: "PDF",
            2: "Images",
            3: "Word",
            4: "Excel",
            5: "Archives",
            6: "Zip_Files",
            7: "PowerPoint"
        }
        
        extensions = file_types[choice]
        folder_name = folder_names[choice]
        
        # Move files
        moved_count = self.move_files(source, dest, extensions, folder_name)
        
        # Update status
        if moved_count > 0:
            self.status_label.config(text=f"Successfully moved {moved_count} files to {folder_name} folder!", fg="green")
            messagebox.showinfo("Success", f"Successfully moved {moved_count} files to {folder_name} folder!")
        else:
            self.status_label.config(text="No matching files found!", fg="red")
            messagebox.showinfo("Info", "No matching files found to organize!")
        
        self.progress['value'] = 100

def main():
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
