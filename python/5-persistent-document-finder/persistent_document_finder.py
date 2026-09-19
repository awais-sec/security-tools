"""
DISCLAIMER: This tool is for EDUCATIONAL PURPOSES ONLY.
It adds itself to system startup and scans the whole drive for
documents on every boot. Run only on systems you own or have explicit
permission to test - this is a persistence-mechanism demo, the same
technique real malware uses to survive a reboot.
"""

import os
import platform
import glob
import sys


def find_files(root_directory, extensions):
    """Searches for files with specific extensions within the given root directory."""
    found_files = []
    for extension in extensions:
        found_files.extend(glob.glob(f'{root_directory}/**/*{extension}', recursive=True))
    return found_files

def save_file_paths(file_paths, output_file="found_files.txt"):
    """Saves the paths of found files to a text file."""
    with open(output_file, 'w') as f:
        for path in file_paths:
            f.write(path + '\n')
    print(f"Paths saved to {output_file}")

def add_to_startup():
    """Adds this script to the system startup process."""
    system_os = platform.system()

    if system_os == "Windows":
        startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        script_path = os.path.abspath(__file__)
        shortcut_path = os.path.join(startup_folder, "FileSearcher.lnk")

        try:
            import win32com.client
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.TargetPath = sys.executable
            shortcut.Arguments = f'"{script_path}"'
            shortcut.WorkingDirectory = os.path.dirname(script_path)
            shortcut.save()
            print("Successfully added to Windows startup.")
        except ImportError:
            print("pywin32 library is required on Windows. Install it with 'pip install pywin32'.")

    elif system_os == "Linux":
        autostart_dir = os.path.expanduser("~/.config/autostart")
        os.makedirs(autostart_dir, exist_ok=True)

        script_path = os.path.abspath(__file__)
        desktop_entry = f"""[Desktop Entry]
Type=Application
Exec={sys.executable} {script_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=FileSearcher
Comment=Search for PDF and DOC files at startup
"""
        desktop_path = os.path.join(autostart_dir, "FileSearcher.desktop")
        with open(desktop_path, 'w') as f:
            f.write(desktop_entry)
        os.chmod(desktop_path, 0o755)
        print("Successfully added to Linux startup.")

    else:
        print("Auto-start setup is not supported for this OS.")

def main():
    add_to_startup()

    system_os = platform.system()
    root_directory = "C:\\" if system_os == "Windows" else "/home/"

    extensions = ['.pdf', '.doc', '.docx']

    print("Searching for files...")
    found_files = find_files(root_directory, extensions)

    print(f"Found {len(found_files)} files with specified extensions.")
    save_file_paths(found_files)

if __name__ == "__main__":
    main()
