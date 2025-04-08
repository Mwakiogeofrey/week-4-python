def modify_content(content):
    # Example: Convert content to uppercase
    return content.upper()

try:
    input_filename = input("Enter the name of the file to read: ")
    
    with open(input_filename, 'r') as file:
        content = file.read()

    modified_content = modify_content(content)

    output_filename = "modified_" + input_filename
    with open(output_filename, 'w') as file:
        file.write(modified_content)

    print(f"Modified content written to '{output_filename}' successfully!")

except FileNotFoundError:
    print(f"❌ Error: The file '{input_filename}' does not exist.")
except IOError as e:
    print(f"❌ IOError: {e}")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
