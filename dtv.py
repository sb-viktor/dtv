import os
import argparse

def print_directory_tree(path, prefix="", show_folders_only=False):
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist or is inaccessible.")
        return

    try:
        entries = sorted(os.listdir(path))
    except Exception as e:
        print(f"Error: Could not read directory '{path}': {str(e)}")
        return

    for i, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        if show_folders_only and not os.path.isdir(full_path):
            continue

        branch = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + branch + entry)

        if os.path.isdir(full_path):
            new_prefix = prefix + ("    " if i == len(entries) - 1 else "│   ")
            print_directory_tree(full_path, new_prefix, show_folders_only)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display directory tree")
    parser.add_argument("directory", help="Path to the directory")
    parser.add_argument("-f", "--include-files", action="store_true",
                        help="Include files in the tree display (default: show only folders)")

    args = parser.parse_args()

    folder_path = os.path.normpath(args.directory)

    print(f"\nDirectory tree for '{folder_path}':")
    print_directory_tree(folder_path, show_folders_only=not args.include_files)