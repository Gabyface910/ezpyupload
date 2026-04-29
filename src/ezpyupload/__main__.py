import PySimpleGUI as sg
import subprocess
import os

def run_workflow(values):
    project_dir = values['-FOLDER-']
    api_token = values['-TOKEN-']
    
    if not project_dir or not os.path.isdir(project_dir):
        print("Error: Please select a valid project directory.")
        return

    os.chdir(project_dir)

    try:
        # 1. Build
        print(f"--- Building in {project_dir} ---")
        subprocess.run(["python", "-m", "build"], check=True, shell=True)

        # 2. Upload
        if api_token:
            print("--- Uploading to PyPI ---")
            env = os.environ.copy()
            env["TWINE_USERNAME"] = "__token__"
            env["TWINE_PASSWORD"] = api_token
            
            # shell=True helps with 'dist/*' expansion on Windows
            subprocess.run(["python", "-m", "twine", "upload", "dist/*"], 
                           env=env, check=True, shell=True)
            print("Success! Package uploaded.")
        else:
            print("Upload skipped: No API token provided.")
            
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")

# --- GUI Layout ---
layout = [
    [sg.Text("Project Directory:"), sg.Input(os.getcwd(), key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Text("PyPI API Token:   "), sg.Input(key="-TOKEN-", password_char="*")],
    [sg.Button("Start Build & Upload"), sg.Button("Exit")],
    [sg.Multiline(size=(60, 10), key="-LOG-", autoscroll=True, disabled=True)]
]

window = sg.Window("Python Package Publisher", layout)

# --- Event Loop ---
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    
    if event == "Start Build & Upload":
        # Redirect print to the Multiline log widget
        window["-LOG-"].update("Starting workflow...\n")
        run_workflow(values)

window.close()
