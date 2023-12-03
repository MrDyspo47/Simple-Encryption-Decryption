import random
import secrets
import  time

alpha = ['as' , 'bd', 'cf', 'd:' , 'e/', 'f!', 'gA', 'Hn', 'iS', 'jQ', 'ke', 'Pk', 'mP', 'nk', 'o<', 'p;', 'qS', 'r!', '?s', 't&', 'uC', 'vP', 'w%', 'xJ', 'yP','zE', '1@' , '2#' , '3!' , '4$' , '5&', '6%' , '7^' , '8*' , '9+' , '0=']
decrypt_key = "F0W8=hMg+l"
firstquestion = input("Do you want to Encrypt or decrypt? E / D : ")
message = input("What is your message : ")
msg = []
mes = []

def encrypt():
  
# ENCRYPTION SIDE OF THE PROGRAM

  if firstquestion == "E" or firstquestion == "e" or firstquestion == "encrypt":
    try:
      for let in message:  # gets each letter in the msg
        if let != " ":  # gets letters that arent space
          msg.append(let) # adds those letters to a list
          wiskey = random.choice(alpha) + let + random.choice(alpha) 
          msg.append(wiskey) # appends the letters to encrypt
          encrypted_text = "".join(msg)
        elif let == " ":
          msg.append("L")
          


      print(encrypted_text)

    except:
        print("There was an error")

#DECRYPTION SIDE OF THE PROGRAM

if firstquestion=="D" or firstquestion=="d" or firstquestion=="decrypt" or firstquestion=="Decrypt" and decrypt_quest == decrypt_key:
  decrypt_quest = input("What is the decryption key ? : ")
  steroids = []
  secretchars = len(message)
  for char in message:
    steroids.append(char)
  for i in range(3, secretchars , 6):
    stiggity = steroids[i] # Puts all of the OG plaintext into a variable
    mes.append(stiggity) # Adds all of the OG plain-text to a list
    decrypted_text = "".join(mes) # Turns the list into a connected string
  print(decrypted_text) 

encrypt() #Function Call




