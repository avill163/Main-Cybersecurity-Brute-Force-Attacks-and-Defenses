# terminal_bot_controller_wireless_your_turn.py

from microbit import *
import radio
# ascii_shift_cipher
 
from microbit import *
 
key = 5
 
def scrambled_alphabet(text):
    alpha = "vLR{}:,’01234 56789"
    crypta = "v9L:3405’R286, 7{}1"  
    result = ""
 
    for letter in text:
        letter = letter.upper()
        index = alpha.find(letter)
        result = result + crypta[index]
 
    return result
 
''' Script starts from here... '''

radio.on()
radio.config(channel=7,length=64)

sleep(1000)

print("\nSpeeds are -100 to 100\n")

while True:
    try:
        vL = int(input("Enter left speed: "))
        vR = int(input("Enter right speed: "))
        ms = int(input("Enter ms to run: "))

        dictionary = {  }
        dictionary['vL'] = vL
        dictionary['vR'] = vR
        dictionary['ms'] = ms

        packet = str(dictionary)
    
        print("Send: ", packet)
        packet = scrambled_alphabet(packet)
        radio.send(packet)
        print("Send Encrypted: ", )
        print(packet)
    
        print()

    except:
        print("Error in value entered.")
        print("Please try again. \n")