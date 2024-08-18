import os
import sys

def print_tree(path, prefix=""):
    """Recursively prints the directory tree structure."""
    try:
        items = os.listdir(path)
        items.sort()
        for i, item in enumerate(items):
            full_path = os.path.join(path, item)
            is_last = i == len(items) - 1
            connector = "\\-- " if is_last else "|-- "
            print(prefix + connector + item)
            if os.path.isdir(full_path):
                new_prefix = prefix + ("    " if is_last else "|   ")
                print_tree(full_path, new_prefix)
    except UnicodeEncodeError:
        # Handle potential encoding issues on different platforms
        print(f"{prefix}|-- (Error: Unable to decode character in filename)")
    except PermissionError:
        print(f"{prefix}|-- (Error: Permission denied)")

if __name__ == "__main__":
    if sys.platform == "win32":
        # For Windows, set the console output encoding to UTF-8
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    main_directory = input("Enter the main directory path: ")
    if os.path.isdir(main_directory):
        print(main_directory)
        print_tree(main_directory)
    else:
        print("Invalid directory path.")
