#
#
#
import const
import telegram
import firebase
import time
import led
#
#
#

def handleCommand(command):
    
    command = command.lower()
    if command == "/ledon":
        led.ledOn()
    elif command == "/ledoff":
        led.ledOff()
    elif command == "/ledtoggle":
        led.ledToggle()
    else:
        print("Invalid Command")
#####################################################################

def handleMessage(message):
    
    idUser = ""
    text = ""
    type = ""
    
    if "message" in message:
        #update_id
        message = message["message"]
        idUser = message["from"]["id"]
        text = message["text"]
        #'entities': [{'offset': 0, 'length': 10, 'type': 'bot_command'}]
        type = message["entities"][0]["type"]
    
    if "bot_command" in type:
        handleCommand(text)
    else:
        print("Message received: " + text)
    print("\r\n")
#####################################################################

def main():

    led.ledExec()
    
    while (True):
        #print(telegram.getMe())
        #print("\r\n')
        #time.sleep(5.0)
        print(telegram.getUpdates())
        print("\r\n")
    #    handleMessage(telegram.getUpdates())
        time.sleep(5.0)

        #firebase.get()
        #time.sleep(5.0)
        #firebase.get(const.FIREBASE_LEDSTATUS)
        #time.sleep(5.0)
        #firebase.get(const.FIREBASE_LAST_MESSAGE)
        #time.sleep(5.0)
        #firebase.get("main")
        #time.sleep(5.0)
    #firebase.set(const.FIREBASE_LEDSTATUS, 1)    
    #telegram.sendMessage()
    #telegram.getMe()
#####################################################################

main()
