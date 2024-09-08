def create_and_write_file():
    try:
        # Open the file in write mode and create it if it doesn't exist
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is George Bush.")
            file.write("A student at PLP Academy.")
            file.write("I am in May Cohort.")
        print("File created and written successfully.")
    except IOError as e:
        print(f"Error while writing to file: {e}")
    finally:
        print("Finished writing to file.")

def read_and_display_file():
    try:
        # Open the file in read mode and display its contents
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except IOError as e:
        print(f"Error while reading the file: {e}")
    finally:
        print("Finished reading from file.")

def append_to_file():
    try:
        # Open the file in append mode and add more lines
        with open("my_file.txt", 'a') as file:
            file.write("I have specialized in several modules.")
            file.write("One of them is python. ")
            file.write("I love to learn python and django to create interacting apps and websites.")
        print("File appended successfully.")
    except IOError as e:
        print(f"Error while appending to file: {e}")
    finally:
        print("Finished appending to file.")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "__main__":
    main()






