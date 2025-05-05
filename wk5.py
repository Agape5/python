def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' was not found.")
        return
    except IOError:
        print(f"❌ Error: Could not read the file '{filename}'.")
        return

    modified_lines = [f"{i + 1}: {line}" for i, line in enumerate(lines)]

    new_filename = f"modified_{filename}"

    try:
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)
        print(f"✅ Modified content has been written to '{new_filename}'")
    except IOError:
        print(f"❌ Error: Could not write to file '{new_filename}'.")

if __name__ == "__main__":
    main()
