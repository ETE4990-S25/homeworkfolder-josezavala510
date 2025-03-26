import os
import hashlib

def hash_file(file_path):
    """Generate MD5 hash for a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(directory):
    """Find duplicate files in a directory."""
    files_hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash in files_hashes:
                duplicates.append((file_path, files_hashes[file_hash]))
            else:
                files_hashes[file_hash] = file_path

    return duplicates

def main():
    while True:
        print("--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            directory = input("Enter directory to search: ")
            if os.path.isdir(directory):
                duplicates = find_duplicates(directory)
                if duplicates:
                    print("Duplicate files found:")
                    for dup in duplicates:
                        print(f"{dup[0]} and {dup[1]}")
                else:
                    print("No duplicate files found.")
            else:
                print("Invalid directory. Please try again.")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()