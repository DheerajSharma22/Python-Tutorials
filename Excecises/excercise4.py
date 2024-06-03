import random
import string

print("Welcome to endecoder.")
choice = int(input("Enter 1 for encode a word or 2 for decode a word :- "))


def generateRandomChars():
    randomChars = random.choices(string.ascii_lowercase, k=3)
    return "".join(randomChars)
    
def encode(words):
    code_list = []
    for word in words:    
        if (len(word) <= 2):
            encoded_word = word[::-1]
            code_list.append(encoded_word)
        else:    
            encoded_word = generateRandomChars() + word[1:] + word[0] + generateRandomChars()
            code_list.append(encoded_word)
    return " ".join(code_list)
            
        

def decode(words):
    code_list = []
    for word in words:    
        if (len(word) <= 2):
            encoded_word = word[::-1]
            code_list.append(encoded_word)
        else:    
            encoded_word = word[-4] + word[3:-4]
            code_list.append(encoded_word)
    return " ".join(code_list)
    

if (choice == 1):
    stringToEncode = input("Enter a word to encode :- ")
    words = stringToEncode.split(" ")
    encoded_secret = encode(words)
    print(f"Your encoded secret is {encoded_secret}")
elif (choice == 2):
    stringToDecode = input("Enter the encoded word you want to decode :- ")
    words = stringToDecode.split(" ")
    decoded_word = decode(words)
    print(f"Your decoded word is {decoded_word}")
else:
    print("Incorrect input")
