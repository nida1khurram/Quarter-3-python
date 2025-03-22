import os

def bulk_rename_files(directory, prefix, start_number=1):
    """
    Rename all files in the specified directory with a given prefix and sequential numbering.

    :param directory: Path to the directory containing the files.
    :param prefix: Prefix to use for the new filenames.
    :param start_number: Starting number for the sequential numbering (default is 1).
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Check if there are any files to rename
    if not files:
        print(f"No files found in the directory '{directory}'.")
        return

    # Sort files to ensure consistent renaming order
    files.sort()

    # Rename files sequentially
    for index, filename in enumerate(files, start=start_number):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]

        # Create the new filename
        new_filename = f"{prefix}_{index}{file_extension}"

        # Get the full paths for the old and new filenames
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

    print("Bulk renaming completed!")

# Example usage
if __name__ == "__main__":
    # Specify the directory containing the files
    directory = r"D:\learning\Quarter-3-python\class-project-sirZia\Project-4-Assignments\Assignments-01\onlineclass-project\06-Bulk-File-Re-namer\nida"

    # Specify the prefix for the new filenames
    prefix = "flower"

    # Specify the starting number (optional, default is 1)
    start_number = 1

    # Call the bulk_rename_files function
    bulk_rename_files(directory, prefix, start_number)