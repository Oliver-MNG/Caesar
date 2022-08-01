alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]

#Murodillo
'''
def caesar(task,text,shift):
    if task == "encode":       
        encoded_text = "" 
        for letter in text:
            position = alphabet.index(letter)
            position_1 = position + shift
            letter_1 = alphabet[position_1]
            encoded_text += letter_1
        print(f"This is the encoded text: '{encoded_text}'")
    elif task == "decode":
        decoded_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            new_letter = alphabet[new_position]
            decoded_text += new_letter
        print(f"This is the decoded text: '{decoded_text}'")
caesar()
'''
again = 'yes'
while again == 'yes':
    text = input("Please input the text:\n")
    shift = int(input('Please input the shift key:\n'))
    task = input('For encryption input "encode", for decryption input "decode":\n')

    def caesar(start_text, shift_amount, dec_or_enc):
        if shift_amount > 26:
            shift_amount = shift_amount % 26
        end_text = ""
        if dec_or_enc == 'decode':
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += letter 
        print(f"This is the {dec_or_enc}d text: {end_text}")
    caesar(start_text = text, shift_amount = shift, dec_or_enc = task)
    again = input("Type 'yes' if you want to go again, 'no' if you don't:\n")


