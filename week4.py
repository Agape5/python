 input_filename = input("Enter the name of the file to read: ")
        
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = content.upper()
        
        output_filename = input("Enter the name of the file to write: ")
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
     except FileNotFoundError:
        print("Error: The file you specified does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read or write to the specified file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_write_file()