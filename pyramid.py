def create_word_pyramid_from_file(file_path):
    """
    Creates a pyramid representation from a text file containing numbers and words.

    Args:
    file_path (str): The path to the text file containing the numbers and words.

    Returns:
    str: A formatted string representing the pyramid of words.
    """
    # Read the file and extract the data
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a dictionary to map numbers to words
    word_dict = {}
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2 and parts[0].isdigit():
            number = int(parts[0])
            word = parts[1]
            word_dict[number] = word  # Map the number to the associated word

    # Generate the expected pyramid structure
    pyramid_levels = []
    current_number = 1
    increment = 1

    # Build the pyramid based on consecutive numbers
    while current_number in word_dict:
        level = []
        for i in range(increment):
            if current_number in word_dict:
                level.append(word_dict[current_number])
                current_number += 1
            else:
                break
        pyramid_levels.append(level)
        increment += 1  # Each subsequent line has one more element

    # Create a formatted pyramid representation
    formatted_pyramid = ""

    # Formatting for visual pyramid
    for i, level in enumerate(pyramid_levels):
        indent = " " * (len(pyramid_levels) - i - 1)  # Indentation for centering
        formatted_pyramid += indent + " ".join(level) + "\n"

    return formatted_pyramid.strip()  # Strip extra newline from the end

# File path to the text file
file_path = r'C:\\Users\\jackr\\Desktop\\coding_qual_input.txt'

# Create and display the pyramid of words
pyramid_representation = create_word_pyramid_from_file(file_path)
print(pyramid_representation)
