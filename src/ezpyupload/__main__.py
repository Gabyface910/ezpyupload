import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys

def handle_paste(event):
    """Explicitly handle pasting from clipboard."""
    try:
        # Get text from clipboard
        text = event.widget.selection_get(selection='CLIPBOARD')
        # Insert at current cursor position
        event.widget.insert(tk.INSERT, text)
    except tk.TclError:
        pass # Clipboard empty or incompatible
    return "break" # Prevent the default paste behavior from doubling the text

def run_command():
    folder = folder_entry.get()
    token = token_entry.get()
    
    if not os.path.isdir(folder):
        messagebox.showerror("Error", "Please select a valid directory.")
        return

    os.chdir(folder)
    
    try:
        print(f"Building in: {folder}")
        subprocess.run([sys.executable, "-m", "build"], check=True)

        if token:
            print("Uploading to PyPI...")
            env = os.environ.copy()
            env["TWINE_USERNAME"] = "__token__"
            env["TWINE_PASSWORD"] = token
            
            # Using glob-like behavior via the shell for the dist/* path
            # On Windows, we call twine via 'python -m twine'
            subprocess.run(f'"{sys.executable}" -m twine upload dist/*', 
                           env=env, check=True, shell=True)
            messagebox.showinfo("Success", "Package uploaded successfully!")
        else:
            messagebox.showwarning("Incomplete", "Build finished, but no token provided.")
            
    except Exception as e:
        messagebox.showerror("Execution Error", str(e))

# --- UI Setup ---
root = tk.Tk()
root.title("Python Publisher")
root.geometry("500x280")

# Folder Selection
tk.Label(root, text="Project Folder:").pack(pady=(10, 0))
folder_frame = tk.Frame(root)
folder_frame.pack()
folder_entry = tk.Entry(folder_frame, width=40)
folder_entry.insert(0, os.getcwd())
folder_entry.pack(side=tk.LEFT, padx=5)

# Bind paste to folder field
folder_entry.bind("<Control-v>", handle_paste)

def browse_folder():
    path = filedialog.askdirectory()
    if path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, path)

tk.Button(folder_frame, text="Browse", command=browse_folder).pack(side=tk.LEFT)

# Token Entry
tk.Label(root, text="PyPI API Token:").pack(pady=(10, 0))
token_entry = tk.Entry(root, width=50, show="*")
token_entry.pack(pady=5)

# Bind paste to token field
token_entry.bind("<Control-v>", handle_paste)
# Support for Right-Click Paste (Windows/Linux)
token_entry.bind("<Button-3>", lambda e: handle_paste(e))

# Action Button
tk.Button(root, text="Build & Upload", bg="#2e7d32", fg="white", 
          command=run_command, height=2, width=20).pack(pady=20)

root.mainloop()
