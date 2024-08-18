# Tree Path

tree-path.py is a Python script that recursively prints the directory tree structure of a specified path. It's a simple and effective way to visualize the hierarchy of files and directories, using ASCII characters for compatibility across different platforms.

## Features

- Recursively prints directory and file structures.
- Handles Unicode and permission errors gracefully.
- Compatible with Windows, macOS, and Linux.
- Uses ASCII characters for broad compatibility.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the tree-path.py script.

```bash
git clone https://github.com/yourusername/yourrepository.git
```

2. Navigate to the directory containing `tree-path.py`.

```bash
cd yourrepository
```

## Usage

1. Run the script using Python.

```bash
python tree-path.py
```

2. Enter the path of the directory you want to visualize when prompted.

```
Enter the main directory path: /path/to/your/directory
```

3. The script will output the directory tree structure.

```
/path/to/your/directory
|-- file1.txt
|-- file2.py
|-- subdirectory
    |-- file3.md
    \-- file4.js
```

## Error Handling

- **UnicodeEncodeError**: If the script encounters a filename with characters that can't be decoded, it will print an error message and continue.
- **PermissionError**: If the script encounters a directory or file that it doesn't have permission to access, it will print an error message and continue.

## Compatibility

- The script is designed to work on Windows, macOS, and Linux.
- For Windows users, ensure your console supports UTF-8 by running `chcp 65001` before executing the script.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or feedback, please contact Your Name.

### Notes:
- Replace yourusername and yourrepository with your actual GitHub username and repository name.
- Update the contact section with your actual name and email address.
- If you have a LICENSE file, make sure to include it in your repository and update the link in the README.md accordingly.

This README.md provides a comprehensive overview of the script, including its features, usage instructions, and other relevant information.
