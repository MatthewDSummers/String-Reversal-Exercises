def reverse_letters_only(input_str):
    letters = [char for char in input_str if char.isalpha()]
    reversed_letters = letters[::-1]
    result = []
    index = 0
    for char in input_str:
        if not char.isalpha():
            result.append(char)
        else:
            result.append(reversed_letters[index])
            index += 1
    return ''.join(result)

print(reverse_letters_only("9Reverse Letters5 only7"))

def reverse_chars_of_words(input_str):
    words_list = input_str.split()
    return ' '.join([word[::-1] for word in words_list])
print(reverse_chars_of_words("Let's reverse each word in their original position"))