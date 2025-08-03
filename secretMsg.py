def mirror_string(string):
    mirrored_string = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                mirrored_char = chr(ord('z') - ord(char) + ord('a'))
            else:
                mirrored_char = chr(ord('Z') - ord(char) + ord('A'))
            mirrored_string += mirrored_char
        else:
            mirrored_string += char
    return mirrored_string.lower()  # Convert the final string to lowercase

# Example usage
input_string = input()
mirrored_string = mirror_string(input_string)

print(mirrored_string)

 



