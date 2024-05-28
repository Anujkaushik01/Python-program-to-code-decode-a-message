'''
Coding:
if the string is at least 3 characters long, remove the first letter and append it to the end, and add 3 random characters at the end and at the start.
else reverse the string.

Decoding:
if the string is at least 3 characters long, remove 3 characters from start and end, and remove the last character and append it to the start.
else reverse the string.
'''

import random
import string


# Function to generate 3 random strings used to code the message.
def random_strings():
    alpha_list = list(string.ascii_lowercase)
    random_chars = ''
    for char in range(3):
        random_chars += random.choice(alpha_list)
    return random_chars


while True:
    message = input('Enter the message: \n')
    message_list = message.split(' ')

    # Asks for input again if it is empty.
    if not message:
        print('Please enter a message to code or decode.')
        continue

    while True:
        action = input('Do you want to code or decode the message? \n')

        # Asks for action again if it is empty.
        if not action:
            print('Please input to code or decode message.')
            continue

        # Checking if action is to code or decode.

        # If action is to code.
        if action.lower() == 'code':
            print('Coding...')
            coded_message = ''
            for word in message_list:
                if len(word) >= 3:
                    word_list = list(word)
                    # Remove last character and places it to the beginning.
                    last_character = word_list.pop()
                    word_list.insert(0, last_character)
                    # Add three characters to the start and to the end.
                    word_list.insert(0, random_strings())
                    word_list.append(random_strings())
                    word = ''.join(word_list)
                    coded_message += word + ' '
                else:
                    # Reverses the word.
                    word_list = list(word)
                    word_list.reverse()
                    word = ''.join(word_list)
                    coded_message += word + ' '
            print(f'Coded message is: \n{coded_message}')

        # If action is to decode.
        elif action.lower() == 'decode':
            print('Decoding...\n')
            decoded_message = ''

            for word in message_list:
                if len(word) >= 9:
                    word_list = list(word)
                    # Removes 3 characters from starting and from end.
                    for _ in range(3):
                        word_list.pop()
                        word_list.reverse()
                        word_list.pop()
                    # Removes last character and places it in front.
                    last_character = word_list.pop()
                    word_list.reverse()
                    word_list.append(last_character)
                    word = ''.join(word_list)
                    decoded_message += word + ' '
                elif len(word) <=2:
                    # Reverses the word.
                    word_list = list(word)
                    word_list.reverse()
                    word = ''.join(word_list)
                    decoded_message += word + ' '
                else:
                    print("Error. Can't decode the message. ")
                    exit()

            print(f'Decoded message is: \n{decoded_message}')
        else:
            print('Please enter to code or decode.')
            continue
        break
    break
