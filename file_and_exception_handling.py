# Creating the file and writing initial content
with open("family_info.txt", "w") as file:
    file.write("My name is Gabriel Ochieng Onyango\n")
    file.write("I am Married to Whitney Gladys Odhiambo\n")
    file.write("We have two children.\n")
    file.write("We stay in Katani, 360 Appartments, Syokimau.\n")

print("✅ 'family_info.txt' has been created successfully.")

# reading and writing from the family_info.txt
def read_and_write_file():
    try:
        filename = input("Enter the filename to read from: ")

        # Trying to open the file in read mode
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Modifying the content (for example, adding line numbers)
        modified_lines = [f"{idx + 1}. {line}" for idx, line in enumerate(lines)]

        # Writing to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)

        print(f"\n✅ Modified file saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you specified does not exist.")
    except IOError:
        print("❌ Error: There was a problem reading the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Runing the function
read_and_write_file()

