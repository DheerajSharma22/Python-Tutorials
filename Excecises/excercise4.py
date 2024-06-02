import random

print("Welcome to endecoder.")
choice = int(input("Enter 1 for encode a word or 2 for decode a word :- "))

def generateRandomChars():
    charList = "abcdefghijklmnopqrstuvwxyz"
    randomChars = random.choice(charList) + random.choice(charList) + random.choice(charList)
    return randomChars
    
def reverse(word):
    reversed_word = ""
    for i in range(len(word)-1, -1, -1):
        reversed_word+=word[i]
    return reversed_word
    
def encode(word):
    if (len(word) <= 2):
        return reverse(word)
        
    encoded_word = word[1:len(word)]
    encoded_word += word[0]
    encoded_word = generateRandomChars() + encoded_word + generateRandomChars()
    return encoded_word

def decode(word):
    if (len(word) <= 2):
        return reverse(word)
    
    decoded_word = word[3:len(word)-4]
    decoded_word = word[len(word)-4] + decoded_word
    return decoded_word
    

if (choice == 1):
    word = input("Enter a word to encode :- ")
    encoded_word = encode(word)
    print(f"Your encoded secret is {encoded_word}")
elif (choice == 2):
    encoded_word = input("Enter the encoded word you want to decode :- ")
    decoded_word = decode(encoded_word)
    print(f"Your decoded word is {decoded_word}")
else:
    print("Incorrect input")
