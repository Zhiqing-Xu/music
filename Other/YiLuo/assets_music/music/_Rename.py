import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if "  " in filename:
            # Remove ' - YiLuo' and add '一萝 - ' at the beginning
            new_filename = filename.replace("  ", " ")

            # Construct full file path
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            # Rename file
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_filename}'")

# Run the function in the current directory
rename_files(".")
