def modify_content(text):
    return text.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return
    except IOError:
        print(f"❌ Error: Could not read file '{filename}'.")
        return

    modified = modify_content(content)

    new_filename = f"modified_{filename}"

    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified)
        print(f"✅ Modified content written to '{new_filename}'")
    except IOError:
        print(f"❌ Error: Could not write to file '{new_filename}'.")

if __name__ == "__main__":
    main()

    