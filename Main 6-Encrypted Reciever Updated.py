# terminal_controlled_bot_wireless

from microbit import *
import radio
# ascii_shift_cipher
 
from microbit import *

 
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

from cyberbot import *
import radio

radio.on()
radio.config(channel=7,length=64)

sleep(1000)

print("Ready...\n")

while True:
    packet = radio.receive()
    if packet is not None:
        packet = ascii_shift(key, packet)
        print("Receive: ", packet)

        dictionary = eval(packet)

        vL = dictionary['vL']
        vR = dictionary['vR']
        ms = dictionary['ms']
        
        bot(18).servo_speed(vL)
        bot(19).servo_speed(-vR)
        sleep(ms)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
        radio.send(packet)
        print("Send Encrypted: ", )
        print(packet)
    
        print()

    except:
        print("Error in value entered.")
        print("Please try again. \n")