def modify_content(content):
    return content.upper()


def main():
    # Ask user for filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create new file name
        new_filename = "modified_" + filename

        # Write modified content to new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Would you like to modify to {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()