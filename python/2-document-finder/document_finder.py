import os
import platform
import glob

def find_files(root_directory, extensions):
    """
    Function to search for files with specific extensions within the given root directory.
    
    Parameters:
    - root_directory (str): The directory to start searching from.
    - extensions (list of str): The list of file extensions to search for.
    
    Returns:
    - found_files (list): A list of paths for all found files matching the given extensions.
    """
    found_files = []
    for extension in extensions:
        # Use glob to find files with the extension in all subdirectories
        found_files.extend(glob.glob(f'{root_directory}/**/*{extension}', recursive=True))
    return found_files

def save_file_paths(file_paths, output_file="found_files.txt"):
    """
    Save the paths of found files to a text file.
    
    Parameters:
    - file_paths (list of str): List of file paths to save.
    - output_file (str): Output file name where file paths will be saved.
    """
    with open(output_file, 'w') as f:
        for path in file_paths:
            f.write(path + '\n')
    print(f"Paths saved to {output_file}")

def main():
    # Determine the root directory based on OS type
    system_os = platform.system()
    if system_os == "Windows":
        root_directory = "C:\\"
    else:
        root_directory = "/home/"

    # Define file extensions to look for
    extensions = ['.pdf', '.doc', '.docx']
    
    # Find files
    print("Searching for files...")
    found_files = find_files(root_directory, extensions)
    
    # Display and save the found file paths
    print(f"Found {len(found_files)} files with specified extensions.")
    save_file_paths(found_files)

if __name__ == "__main__":
    main()
