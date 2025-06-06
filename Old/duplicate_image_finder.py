# duplicate_image_finder.py



import os
import sys
import hashlib

def hash_file(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def find_duplicates(folder_path, output_path):
    seen_hashes = {}
    with open(output_path, 'w') as output:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_hash = hash_file(file_path)
                    if file_hash in seen_hashes:
                        output.write(f"{file_path}, {file_hash}\n")
                    else:
                        seen_hashes[file_hash] = file_path
                except Exception as e:
                    print(f"Error hashing {file_path}: {e}")

if __name__ == '__main__' and len(sys.argv) == 3:
    folder = sys.argv[1]
    save_to = sys.argv[2]
    find_duplicates(folder, save_to)
else:
    print("Usage: python script.py <folder_path> <output_file>")