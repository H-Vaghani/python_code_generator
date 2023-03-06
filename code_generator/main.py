import random
def encoded(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_text = ""
    for letter in text:
        if letter in alphabet:
            new = random.choice(alphabet)
            encoded_text += new
        else:
            encoded_text += letter

    return encoded_text

def text_to_encode():
    message  = input("Enter text to encode: ")
    message.lower()
    encoded_message = encoded(message)
    print(encoded_message)
    menu()


def menu():
    new_text = input("To Encode new text press X ")
    x = new_text
    while True:
        if x == "x" or x == "X":
            text_to_encode()
        else:
            print("thanks you")
            exit()



text_to_encode()
