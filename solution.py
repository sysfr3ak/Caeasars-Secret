import resources

def decrypt(flag_text, shift):
    output = ""
    for letter in flag_text:
        if letter in resources.alphabet:
            shift_position = resources.alphabet.index(letter) - shift
            shift_position %= len(resources.alphabet)
            output += resources.alphabet[shift_position]
        else:
            output += letter
    return output

decrypted_values = []
potential_flags = []
flag_counter = 0
while flag_counter < len(resources.flags):
    flag = resources.flags[flag_counter].lower()
    shifting = 0
    while shifting < 26:
        current_shift = shifting
        decrypted_output = decrypt(flag_text=flag, shift=current_shift)
        decrypted_values.append(decrypted_output)
        shifting += 1
    flag_counter += 1

for word in resources.dictionary:
    for string in decrypted_values:
        if word in string.lower().split():
            potential_flags.append(string)
print(potential_flags)