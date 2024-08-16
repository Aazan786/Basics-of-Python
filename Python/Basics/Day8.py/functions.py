#prime number checker

# def prime_no_check(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False

#     if is_prime:
#         print("Number is prime")
#     else:
#         print("Number is not prime")    

   
# number =int(input("Enter number: "))
# prime_no_check(number)

#Ceaser Cipher program

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type encode to encrypt and decode to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(cipher_text)    

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decipher_text += new_letter
#     print(plain_text)


# if direction == "encode":
#     encrypt(plain_text = text, shift_amount = shift)
# if direction == "decode":   
#     decrypt(cipher_text= cipher_text, shift_amount = shift)


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
    print(f"{direction}: {output_text}")   

def Restart():
    again = input("would you like to restart the cipher program? Type Yes or No: ")
    if again == "yes":
        direction = input("Type encode to encrypt and decode to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        Ceaser(input_text = text, shift_amount = shift, cipher_direction = direction)
    else:
        print("Good Bye")    
        
Ceaser(input_text = text, shift_amount = shift, cipher_direction = direction)
Restart()