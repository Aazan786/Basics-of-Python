from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 
'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c',
'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o','p', 'q', 'r', 's', 
't', 'u', 'v', 'w', 'x', 'y', 'z']

def Ceaser(input_text, shift_amount, cipher_direction):
    output_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            output_text += new_letter
        else:
           output_text += char   
    print(f"Your {direction}d message is: {output_text}")

def Restart():
    Continue = input("would you like to restart the cipher program? Type Yes or No: ")
    if Continue == "yes":
        direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Enter the shift number:\n"))
        shift = shift % 26
        Ceaser(input_text = text, shift_amount = shift, cipher_direction = direction)
    else:
        print("Good Bye")    

 
direction = input("Type 'encode' to encrypt, Type'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Enter the shift number:\n"))
shift = shift % 26

Ceaser(input_text = text, shift_amount = shift, cipher_direction = direction)
Restart()

