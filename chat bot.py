#  import some modoule

import os, time
import random
import sys

# Now create this words for incoming
nameIn=["what is your name",'what is name',"whats your name","what is your name?","whats your name?"]
greetIn=["hello","hi","hi there","hello there"]
birth=["what is your date of birth","date of birth","what is your date of birth?","what is your DOB","what is your DOB?"]
botmaster=["who is your boat master","who is your boot master?","who is your father","who is your mother","who created you"]

# This word for outcoming
greetOut=["hi there","hello","hi my name is v2","hello there"]
nameOut=["i am called vitthal","my name is v2","hello myself vit","im called vitthal"]



B='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
print(B)
while True:
    H=raw_input('=>').strip()
    HLower=H.lower()

    if H=='':
           print '=> Thanks meeting you'
           time.sleep(1)
           os.system("sudo shut down -h now")
           break
    elif HLower in nameIn:
        print '=>' +( random.choice(nameOut))
    elif HLower in greetIn:
        print '=>' + ( random.choice(greetOut))
    elif HLower in botmaster:
        print '=> my botmaster is vitthal'
    elif HLower in birth:
        print '=> I was activated in the 8 th December 2018'


 # Let test out chat bot        
           

           

           
