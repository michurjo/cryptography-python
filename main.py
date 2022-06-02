from slowprint import slowprint
import string
import os
import json
import time
from cryptography.fernet import Fernet
def clear(x):
  time.sleep(x)
  os.system('clear')
#https://replit.com/@mjiaotcss/fernet-test#main.py

#check the link above for reference or toying around with code

def NBIF(string): #no byte in front
  string = string.replace("\'","")
  return(string[1:])

  
#code below is generating and ungenerating a message
"""key = Fernet.generate_key()
cipher_suite = Fernet(key)

encoded_text = cipher_suite.encrypt(b"test message")
print(encoded_text)
decoded_text = cipher_suite.decrypt(encoded_text)
print(decoded_text)"""





slowprint("\033[1;91m" + "Welcome to the Text Encryptor.",0.05)

print("\n"+"\033[0m")

slowprint("Would you like to add an encryption message\nor decrypt an existing one?\n(respond with encrypt or decrypt)\n\n",0.05)
firstchoice = str(input("-> ")).strip()
if firstchoice == "encrypt":
  
  print("Awesome choice. What do you want your file name tobe?\n")
  filename = str((input("-> ").strip()).replace(" ",""))
  newfile = open(filename + ".txt", "x")
  slowprint("Great. The file has been created.",0.05)
  
  slowprint("\n\nPlease write the message you want, and enter the ENTER key when you are done.",0.05)
  message = input("\nENTER MESSAGE -> ")
  slowprint("We added the encoded message into the text file.",0.05)

  clear(2)

  f = open(filename + ".txt", "a")
  
  key = Fernet.generate_key()
  cipherkey = Fernet(key)
  encoded_text = cipherkey.encrypt((message).encode('UTF-8'))
  f.write(NBIF(str(encoded_text)))
  f.close()
  slowprint("Your key is: " + "\033[1;91m" + NBIF(str(key)),0.05)
  slowprint("\n\nYou need to keep this key somewhere safe, as it is impossible to decode a message without it.",0.05)
  slowprint("\n\nYou can send the key to your friend to read the message, or hold on to it so you can read it later.",0.05)
  exit(0)
  
  


elif firstchoice == "decrypt":
  print("Alright, I hope you have the key for the file. What file are you going to be decrypting?")
  print("\n(Just write the name of the file, without the .txt at the end.)\n\n")
  filename = input("-> ")
  f = open(filename + ".txt","r")
  message = f.read()
  key = Fernet(input("What is the encryption key?\n-> "))
  try:
    decoded_text = key.decrypt(message.encode("UTF-8"))
  except:
    slowprint("\033[1;91m"+"wrong key. process aborted.",0.1)
    exit(0)
  clear(1.5)
  print("Your message is below.\n\n")
  print("\033[1;91m" + NBIF(str(decoded_text)))
  print("\n\nClick ENTER to delete the file.")
  deletefile = input("-> ")
  os.remove(filename + ".txt")
  

  
  
  




