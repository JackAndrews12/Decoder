def decode(message_file):
    """
    This decodes a message based on a "pyramid" structure.
    The function identifies the word associated with the number at the end of each pyramid line.

    Args:
    message_file (str): The path to the .txt file containing the encoded message.

    Returns:
    str: The decoded message as a concatenated string.
    """
    with open(message_file, 'r') as file:
        # Read the lines and extract the numbers and words
        lines = file.readlines()

    # Store the words and their corresponding numbers in a dictionary
    word_dict = {}
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 2 and parts[0].isdigit():
            number = int(parts[0])
            word = parts[1]
            word_dict[number] = word  # Map number to its corresponding word

    # Define the expected pyramid endpoints (e.g., 1, 3, 6, etc.)
    pyramid_endpoints = []
    current_number = 1
    increment = 1

    # Build the pyramid structure to identify the correct sequence
    while current_number in word_dict:
        pyramid_endpoints.append(current_number)
        increment += 1
        current_number += increment

    # Extract the words for the decoded message
    decoded_words = [word_dict[endpoint] for endpoint in pyramid_endpoints]

    # Join the words to create the final decoded message
    decoded_message = " ".join(decoded_words)

    return decoded_message

file_path = r'C:\\Users\\jackr\\Desktop\\coding_qual_input.txt'

decoded_message = decode(file_path)
print(decoded_message)
