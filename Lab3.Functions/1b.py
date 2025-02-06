from cryptography.fernet import Fernet

# will be encrypting the below string
message = input("Enter a string to encrypt: ")

# generating a key for encryption and decryption 
# can use fernet to genreate a key or using a random key generator (but in this case using fernet)
key = Fernet.generate_key()

# Instance the fernet class with the key
fernet = Fernet(key)

# using the fernet class instance in order to encrypt the string must be encoded to byte string before the encryption
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()
# decrypting 
print("decrypted string: ", decMessage)