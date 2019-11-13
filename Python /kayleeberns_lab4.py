def get_shift_input():
    try:
        number = int(input('Enter a number 1-26:  '))
        if number in range(1, 27):
            return number
        else:
            print("Invalid number")
            return get_shift_input()
    except:
        print("not a valid input")
        return get_shift_input()


if __name__ == "__main__":

    requested_shift = get_shift_input()

    original_file = open('kayleeberns_lab4_original.txt')
    original_message = original_file.readlines()

    encrypted_file = open('kayleeberns_lab4_encrypted.txt', 'w')

    for line in original_message:
        words = line.split()
        encrypted_line = ""
        for word in words:
            encrypted_word = ""
            for char in word.lower():
                encrypted_word += chr(((ord(char) + requested_shift - 97) % 26) + 97)

            encrypted_line += " "
            encrypted_line += encrypted_word

        encrypted_line += '\n'
        encrypted_file.write(''.join(encrypted_line))
