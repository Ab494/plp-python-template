# Ask the user to enter the file name
file_name = input("Enter the file name to read (e.g., input.txt): ")
try:
    # open the file and read its contents
    file = open(file_name, 'r')
    content = file.read()
    
    # Convert the content to uppercase
    upper_content = content.upper()
    print("Content in uppercase:")
    print(upper_content)
    
    
    # count words in the content
    words =content.split()
    word_count = len(words)
    print("Word count:", word_count)
    
    
    # Write the result to a new file
    output = open("output.txt", 'w')
    output.write("Processed Content:\n")
    output.write(upper_content + "\n") # Write uppercase content
    output.write(f"Word count: {word_count}")
    
    # Close files
    file.close()
    output.close()
except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")
    
    
    
    
    
    
    
    
    