import random
import string



def encrypt():
     # ENCRYPT
    plain_text=input("enter the plain text:")
    cipher_text= ""
    for letter in plain_text:
          index=chars.index(letter)
          cipher_text +=keys[index]
    
    print(f"The plain text is :{plain_text}")
    print(f"The cipher text is : {cipher_text}")


#DECRYPT
def decrypt():
    cipher_text=input("enter the cipher text:")
    plain_text= ""
    for letter in cipher_text:
          index=keys.index(letter)
          plain_text +=chars[index]
    
    
    print(f" the cipher text is : {cipher_text}")
    print(f"The plain text is :{plain_text}")

chars=" " +string.punctuation +string.digits +string.ascii_letters
chars=list(chars)
keys=chars.copy()

random.shuffle(keys)

#print(f"chars: {chars}")
#print(f"keys: {keys}")
encrypt()
decrypt()